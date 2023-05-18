from dash import Dash, dcc, html
import dash_bootstrap_components as dbc

import pandas as pd

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Card([
        dbc.CardBody([
            html.H1("Hello From Dash in a new environment!"),
            html.Hr(),
            html.P("I created an environment for this dashboard")
        ])
    ],
    className="mt-3"
    )

])

if __name__ == '__main__':
    app.run_server(debug = True)