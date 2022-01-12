# imports
import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import json


# This is where we create the Dash App
app = dash.Dash(__name__)


# This is a Dataframe - it contains tabular data
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

# see https://plotly.com/python/px-arguments/ for more options
fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")


# The layout holds all the components of your app
# Everything is in one html div Component
app.layout = html.Div(children=[
    html.H1(children='Hello Dash!'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])


# entry point of the application
if __name__ == '__main__':
    app.run_server(debug=True)