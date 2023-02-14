"""
Author: Sunil Jaideep Danda.
Date : 13-02-2023
"""
import datetime
import psycopg2
import dash
from dash import dcc
from dash import html
from dash.dependencies import Output, Input, State
from dash.exceptions import PreventUpdate
from Pages import employee_page, reset_password_page, signup_page, information_page, about_page
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
        ]),
        html.Br(),
        dbc.Row([
            dbc.Col(dcc.Link("Forgot Password", id='reset', href="/forgot_password")),
            dbc.Col(dcc.Link("Signup", id='signup', href="/signup_account")),
        ]),
        html.Br(),
        html.Div(id='login_output')
    ], style=from_style),

])


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
    elif pathname == '/signup_account':
        return signup_page.layout
    elif pathname == '/information_page':
        return information_page.layout
    elif pathname == '/about_page':
        return about_page.layout
    else:
        return home_page


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


@app.callback(
    Output('reset_login_output', 'children'),
    [Input('password_change', 'n_clicks')],
    [State('user_name_reset', 'value'), State('user_password_reset', 'value')])
def reset_output(n, user_name, user_password):
    if n is None:
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
        else:
            update_login_table(user_name, user_password)
            return dbc.Alert("Password updated", color="success")


def update_login_table(user_name, password):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="admin",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="dash_assignment")

        cursor = connection.cursor()

        print("Table Before updating record ")
        sql_select_query = """select * from dash_schema.login_meta_table where username = %s"""
        cursor.execute(sql_select_query, (user_name,))
        record = cursor.fetchone()
        print(record)

        # Update single record now
        sql_update_query = """Update dash_schema.login_meta_table set password = %s where username = %s"""
        cursor.execute(sql_update_query, (password, user_name))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record Updated successfully ")

        print("Table After updating record ")
        sql_select_query = """select * from Update dash_schema.login_meta_table where username = %s"""
        cursor.execute(sql_select_query, (user_name,))
        record = cursor.fetchone()
        print(record)

    except (Exception, psycopg2.Error) as error:
        print("Error in update operation", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


@app.callback(
    Output('signup_output', 'children'),
    [Input('password_set', 'n_clicks')],
    [State('user_name_set', 'value'), State('user_password_set', 'value')])
def reset_output(n, user_name, user_password):
    if n is None:
        raise PreventUpdate
    else:
        if user_name == '' or user_name is None or user_password == '' or user_password is None:
            return dbc.Alert("Username/ password is empty please try again", color="warning")
        else:
            insert_login_table(user_name, user_password)
            return dbc.Alert("Account created", color="success")


def insert_login_table(user_name, user_password):
    import psycopg2

    try:
        connection = psycopg2.connect(user="postgres",
                                      password="admin",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="dash_assignment")
        cursor = connection.cursor()

        postgres_insert_query = """ INSERT INTO dash_schema.login_meta_table VALUES 
        (%s,%s,%s,%s,%s,%s)"""
        record_to_insert = (user_name, user_password, datetime.datetime.now(), datetime.datetime.now(),
                            user_name, user_name)
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into login meta table")

    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into login meta table", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


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
            style_cell={
                'textOverflow': 'ellipsis',
                'overflow': 'hidden'
            },
            style_data={
                'whiteSpace': 'normal',
                'height': 'auto',
            }
        )


@app.callback(
    [Output('container', 'children')],
    [Input('filter_department_button_additional', 'n_clicks')])
def dropdown_display(n):
    if n is None:
        raise PreventUpdate
    else:
        url = 'postgresql+psycopg2://postgres:admin@127.0.0.1:5432/dash_assignment'
        engine = sqlalchemy.create_engine(url)
        sql = '''
                SELECT * FROM dash_schema.employee_dept;
            '''
        with engine.connect().execution_options(autocommit=True) as conn:
            query = conn.execute(text(sql))

        df = pd.DataFrame(query.fetchall())
        department_values = df['department'].unique()
        div = html.Div([
            dbc.Row([dbc.Col(
                dcc.Dropdown(
                    id='department_selection_new',
                    placeholder="Select the Department",
                    options=[{'label': x, 'value': x} for x in department_values]
                )),
                dbc.Col(html.Div(dbc.Button('filter', id='filter_department_button_new', color='info')),
                        width='auto')
            ])])
        return div,


@app.callback(
    Output('new_container', 'children'),
    [Input('filter_department_button_new', 'n_clicks'),
     Input('department_selection_new', 'value')],
    State('department_selection', 'value')
)
def department_table_render_new(n, dept_new, dept):
    """
    Callback to display joined data table
    """
    if n is None:
        raise PreventUpdate
    else:
        if dept_new == dept:
            return dbc.Alert('Please select a different department from the above', color='warning')
        else:
            df = data_render(dept_new)
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
                style_cell={
                    'textOverflow': 'ellipsis',
                    'overflow': 'hidden'
                },
                style_data={
                    'whiteSpace': 'normal',
                    'height': 'auto',
                }
            )


if __name__ == '__main__':
    app.run_server(debug=True)
