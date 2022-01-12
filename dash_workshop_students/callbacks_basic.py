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


app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Lets learn callbacks!"),
    #html.H3("How much do you like 🍫?"),
    #dcc.Slider(
    #id='choc-input',
    #min=1,
    #max=10,
    #step=1,
    #marks={
    #    1: '1',
    #    3: '3',
    #    5: '5',
    #    7: '7',
    #    10: {'label': 'YES','style': {"font-weight": "bold"}}
    #},
    #value=0),
    #html.Br(),
    #html.Div(id='my-output'),

    html.H3("you can only choose one thing: emojee"),
    dcc.Dropdown(
        id='emoji-input',
        options=[
            {"label":"😳","value": "ayo sus"},
            {"label":"😭","value": "dats sad"},
            {"label":"🏃‍♀️💨","value": "brb dashing"},
        ]
        ),
    html.Br(),
    html.Div(id='emoji-output'),

])

#challenge: instead of using a slider, use a dcc.Dropdown component to achieve the same effect


@app.callback(
    #Output(component_id='my-output', component_property='children'),
    #Input(component_id='choc-input', component_property='value')
    Output(component_id='emoji-output', component_property='children'),
    Input(component_id='emoji-input', component_property='value')
)
def update_output_div(input_value):
    #if input_value == "😳":
    #    input_value = 100
    #return f"Here's {'🍫'*input_value} chocolates!"
    return f"Ayo..? {input_value}!"

if __name__ == '__main__':
    app.run_server(debug=True)
