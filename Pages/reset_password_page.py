import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input, State
from dash.exceptions import PreventUpdate
from Pages import employee_page, reset_password_page
import dash_bootstrap_components as dbc
import sqlalchemy
from sqlalchemy.sql import text
import pandas as pd

from_style = {'margin-left': '35%', 'width': '450px',
              'height': '45px', 'padding': '10px',
              'margin-top': '60px', 'font-size': '16px',
              'border-width': '3px', 'border-color': '#a0a3a2'
              }

layout = html.Div([
    html.Br(),
    html.Div([
        dcc.Markdown(''' Please reset your password by giving your user name below '''),
        dbc.Input(id="user_name_reset", placeholder="Enter Username", type="text"),
        html.Br(),
        dbc.Input(id="user_password_reset", placeholder="Enter New Password", type="text"),
        html.Br(),
        dbc.Row([
            dbc.Button("Change Password", id='password_change', size="lg", className="d-grid gap-2 col-6 mx-auto"),
        ]),
        html.Br(),
    ], style=from_style),

])

# @app.callback(
#     Output('login_output', 'children'),
#     [Input('verify', 'n_clicks')],
#     [State('user_name', 'value'), State('user_password', 'value')])
# def update_output(n_clicks, user_name, user_password):
#     """
#     :param n_clicks: Login Button verifies the credentials.
#     :param user_name:  checks for username exists in table
#     :param user_password:  checks for password match
#     :return: login output based on callback.
#     """
#     if n_clicks is None:
#         raise PreventUpdate
#     else:
#         url = 'postgresql+psycopg2://postgres:admin@127.0.0.1:5432/dash_assignment'
#         engine = sqlalchemy.create_engine(url)
#         sql = '''
#                 SELECT * FROM dash_schema.login_meta_table;
#             '''
#         with engine.connect().execution_options(autocommit=True) as conn:
#             query = conn.execute(text(sql))
#
#         df = pd.DataFrame(query.fetchall())
#         credentials = dict(zip(df.username, df.password))
#         if user_name == '' or user_name is None or user_password == '' or user_password is None:
#             return dbc.Alert("Username/ password is empty please try again", color="warning")
#         if user_name not in credentials:
#             return dbc.Alert("Incorrect Username", color="warning")
#         if credentials[user_name] == user_password:
#             return dcc.Location(pathname="/employee_page", id="employee_page_id")
#         else:
#             return dbc.Alert("Incorrect Password", color="warning")
