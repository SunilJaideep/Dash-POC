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
        dcc.Markdown(''' Please provide username and password below '''),
        dbc.Input(id="user_name_set", placeholder="Enter Username", type="text"),
        html.Br(),
        dbc.Input(id="user_password_set", placeholder="Enter Password", type="text"),
        html.Br(),
        dbc.Row([
            dbc.Button("Signup", id='password_set', size="lg", className="d-grid gap-2 col-6 mx-auto"),
        ]),
        html.Br(),
        html.Div(id='signup_output')
    ], style=from_style),

])