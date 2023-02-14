from dash import dcc
from dash import html
from dash import dash_table
import dash_bootstrap_components as dbc
import sqlalchemy
from sqlalchemy.sql import text
import pandas as pd

url = 'postgresql+psycopg2://postgres:admin@127.0.0.1:5432/dash_assignment'
engine = sqlalchemy.create_engine(url)
sql1 = '''
    SELECT * FROM dash_schema.employee_dept;
'''
sql2 = '''
    SELECT * FROM dash_schema.employee_info;
'''
with engine.connect().execution_options(autocommit=True) as conn:
    query = conn.execute(text(sql1))
    query2 = conn.execute(text(sql2))
df = pd.DataFrame(query.fetchall())
df = df.drop('department_id', axis=1)
df2 = pd.DataFrame(query2.fetchall())
df = df.merge(df2, on='employee_id', how='inner')
df = df.drop(['employee_id', 'employee_name'], axis=1)
output = df.groupby(['department'], as_index=False).agg({'employee_salary': ['mean']})
output.columns = ['department', 'average_salary']

layout = dbc.Container([
    html.Br(),
    dbc.Row([
        html.Br(),
        dbc.Card([
            dbc.CardHeader(
                html.Center(html.H1("Information Page"))
            ),
            dbc.CardBody([
                html.Div([
                    html.Br(),
                    dbc.Row([
                        html.Div(id='Average_table_display',
                                 children=[dash_table.DataTable(
                                     data=output.to_dict('records'),
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
                                 )])
                    ]),
                    html.Br(),
                ]),
            ])
        ]),
    ])
])
