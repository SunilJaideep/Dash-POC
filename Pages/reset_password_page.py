import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

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
        html.Div(id='reset_login_output')
    ], style=from_style),

])
