import dash_bootstrap_components as dbc
from dash import html

"""
Navbar or Header for the dashboard
"""
navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                dbc.Row(
                    dbc.Col(dbc.NavbarBrand("POC Dashboard", className="ms-2")),
                    align="center",
                    className="g-0",
                ),
                href="/",
                style={"textDecoration": "none"},
            ),
            dbc.Row(
                [
                    dbc.NavbarToggler(id="navbar-toggler"),
                    dbc.Collapse(
                        dbc.Nav(
                            [
                                dbc.NavItem(html.Img(src='/static/src/usefulbi_logo.jpg',
                                                     className='logo', height="60px", width="100px"),
                                            className="me-auto"
                                            ),
                                dbc.NavItem(dbc.NavLink("Source Code", href="https://github.com/SunilJaideep/Dash-POC")),
                                dbc.NavItem(dbc.NavLink("About", href='/about_page')),
                            ],

                            className="w-100",
                        ),
                        id="navbar-collapse",
                        is_open=False,
                        navbar=True,
                    ),
                ],
                className="flex-grow-1",
            ),
        ],
        fluid=True,
    ),
    dark=True,
    color="dark",

)

