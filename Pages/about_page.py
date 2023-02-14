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
        html.Br(),
        html.Div([
            dbc.Row([
                html.H1("Author: Sunil Jaideep Danda"),
                html.H3("Purpose: POC Assignment for UsefulBI :)")
            ])
        ]),
        html.Br(),
        dcc.Markdown('''Note: This is a Sample POC application fro learning purpose '''),
        html.Br(),
    ], style=from_style),

])
