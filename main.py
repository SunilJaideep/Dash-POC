"""
Author: Sunil Jaideep Danda.
Date : 13-02-2023
"""

import dash
from dash import dcc
from dash import html
from dash.dependencies import Output, Input, State
from dash.exceptions import PreventUpdate
from Pages import employee_page, reset_password_page
import dash_bootstrap_components as dbc
from Navbar import navbar
import sqlalchemy
from sqlalchemy.sql import text
import pandas as pd
from dash import dash_table

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content')
])

from_style = {'margin-left': '35%', 'width': '450px',
              'height': '45px', 'padding': '10px',
              'margin-top': '60px', 'font-size': '16px',
              'border-width': '3px', 'border-color': '#a0a3a2'
              }

home_page = html.Div([
    html.Br(),
    html.Div([
        dcc.Markdown(''' Hi Welcome to POC Dashboard of Useful BI please login! '''),
        dbc.Input(id="user_name", placeholder="Enter Username", type="text"),
        html.Br(),
        dbc.Input(id="user_password", placeholder="Enter Password", type="text"),
        html.Br(),
        dbc.Row([
            dbc.Button("Login", id='verify', size="lg", className="d-grid gap-2 col-6 mx-auto"),
            dcc.Link("Forgot Password", id='reset', href="/forgot_password"),
        ]),

        html.Br(),
        html.Div(id='login_output')
    ], style=from_style),

])


@app.callback(
    Output('login_output', 'children'),
    [Input('verify', 'n_clicks')],
    [State('user_name', 'value'), State('user_password', 'value')])
def update_output(n_clicks, user_name, user_password):
    """
    :param n_clicks: Login Button verifies the credentials.
    :param user_name:  checks for username exists in table
    :param user_password:  checks for password match
    :return: login output based on callback.
    """
    if n_clicks is None:
        raise PreventUpdate
    else:
        url = 'postgresql+psycopg2://postgres:admin@127.0.0.1:5432/dash_assignment'
        engine = sqlalchemy.create_engine(url)
        sql = '''
                SELECT * FROM dash_schema.login_meta_table;
            '''
        with engine.connect().execution_options(autocommit=True) as conn:
            query = conn.execute(text(sql))

        df = pd.DataFrame(query.fetchall())
        credentials = dict(zip(df.username, df.password))
        if user_name == '' or user_name is None or user_password == '' or user_password is None:
            return dbc.Alert("Username/ password is empty please try again", color="warning")
        if user_name not in credentials:
            return dbc.Alert("Incorrect Username", color="warning")
        if credentials[user_name] == user_password:
            return dcc.Location(pathname="/employee_page", id="employee_page_id")
        else:
            return dbc.Alert("Incorrect Password", color="warning")


@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    """
    :param pathname: url of the page being loaded
    :return: contents of the page in loaded url
    """
    if pathname == '/employee_page':
        return employee_page.layout
    elif pathname == '/forgot_password':
        return reset_password_page.layout
    else:
        return home_page


def data_render(dept):
    """
    :param dept: department name as input
    :return: data from the tables employee and department joined.
    """
    url = 'postgresql+psycopg2://postgres:admin@127.0.0.1:5432/dash_assignment'
    engine = sqlalchemy.create_engine(url)
    sql1 = '''
                    SELECT * FROM dash_schema.employee_dept;
                    '''
    sql2 = '''
                    SELECT * FROM dash_schema.employee_info;
                    '''
    with engine.connect().execution_options(autocommit=True) as conn:
        query1 = conn.execute(text(sql1))
        query2 = conn.execute(text(sql2))
    emp_dpt = pd.DataFrame(query1.fetchall())
    emp_dpt = emp_dpt[emp_dpt['department'] == dept]
    emp_info = pd.DataFrame(query2.fetchall())
    df = emp_dpt.merge(emp_info, on='employee_id')
    df = df.drop('department_id', axis=1)
    df = df[['employee_id', 'employee_name', 'department', 'employee_salary']]
    return df


@app.callback(
    Output('filter_table_display', 'children'),
    [Input('filter_department_button', 'n_clicks'),
     Input('department_selection', 'value')]
)
def department_table_render(n, dept):
    """
    Callback to display joined data table
    """
    if n is None:
        raise PreventUpdate
    else:
        df = data_render(dept)
        return dash_table.DataTable(
            data=df.to_dict('records'),
            row_selectable="multi",
            # row_selectable='multi',
            selected_rows=[],
            style_header={
                'backgroundColor': 'rgb(230, 230, 230)',
                'fontWeight': 'bold'
            },
            style_table={
                'maxHeight': '300px',
                'overflowY': 'scroll'
            },
            fixed_rows={
                'headers': True,
                'data': 0
            }
            # page_action='native',
            # page_size=10,
        )


@app.callback(
    [Output('filter_dropdown_display', 'children')],
    [Input("filter_department_button", "n_clicks")],
    State("filter_table_display", "selected_rows"),
    prevent_initial_call=True,
)
def department_table_render_additional(n, derived_virtual_selected_rows):
    """
    Callback to display joined data table
    """
    print(derived_virtual_selected_rows)
    if n:
        if len(derived_virtual_selected_rows) >= 1:
            plus_button = dbc.Row([
                html.Div(dbc.Button('Check More +', id='filter_department_button_additional', color='info')),
            ])
            return plus_button
    else:
        return dash.no_update


if __name__ == '__main__':
    app.run_server(debug=True)
