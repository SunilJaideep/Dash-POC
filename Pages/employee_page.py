import dash
from dash import dcc
from dash import html
from dash import dash_table
from dash.dependencies import Output, Input, State
from dash.exceptions import PreventUpdate
from Pages import employee_page, reset_password_page
import dash_bootstrap_components as dbc
import sqlalchemy
from sqlalchemy.sql import text
import pandas as pd
from main import app

from_style = {'margin-left': '35%', 'width': '450px',
              'height': '45px', 'padding': '10px',
              'margin-top': '60px', 'font-size': '16px',
              'border-width': '3px', 'border-color': '#a0a3a2'
              }

url = 'postgresql+psycopg2://postgres:admin@127.0.0.1:5432/dash_assignment'
engine = sqlalchemy.create_engine(url)
sql = '''
        SELECT * FROM dash_schema.employee_dept;
    '''
with engine.connect().execution_options(autocommit=True) as conn:
    query = conn.execute(text(sql))

df = pd.DataFrame(query.fetchall())
department_values = df['department'].values

layout = dbc.Container([
    html.Br(),
    dbc.Row([
        html.Br(),
        dbc.Card([
            dbc.CardHeader(
                html.Center(html.H1("Employee Page"))
            ),
            dbc.CardBody([
                html.Div([
                    dbc.Row([dbc.Col(
                        dcc.Dropdown(
                            id='department_selection',
                            placeholder="Select the Department",
                            options=[{'label': x, 'value': x} for x in department_values]
                        )),
                        dbc.Col(html.Div(dbc.Button('filter', id='filter_department_button', color='info')),
                                width='auto')
                    ]),
                    html.Br(),
                    dbc.Row([
                        html.Div(id='filter_table_display', children=[dash_table.DataTable(id='render_filter_table')])
                    ]),
                    # dbc.Row([
                    #     html.Div(dbc.Button('Check More +', id='filter_department_button_additional', color='info'))
                    # ]),
                    dbc.Row([
                        html.Div(id='filter_dropdown_display', children=[])
                    ]),
                ]),
            ])
        ]),
    ])
])
