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


# boston housing dataset
df = pd.read_csv("datasets/housing_processed.csv")

# see https://plotly.com/python/px-arguments/ for more options
# replace None with code to produce a px scatterplot (use any x and y you like from the boston dataset)
# feel free to try out 3d plots if you like
fig = px.scatter_3d(df, x='CRIM', y='B', z='MEDV')


# The layout holds all the components of your app
# Everything is in one html div Component
app.layout = html.Div(children=[
    ### use some html header (H1-6)
    html.H2(children="Dash! Except I'm dashing away from responsibilities"),

    ### use a html break to leave some space
    html.Br(),
    ### use a html div to give a description of your app (or just put your name)
    html.Div(children='''
        Hey this kinda works!
    '''),
    ### use the graph component from dash core components to display the graph from above (fig)
    #dcc.Graph(figure = fig, x="crime rate per capita by town", y="nitric oxides concentration (parts per 10 million)", z="hehe"), #needs fix

    ### use the slider component from dash core components to make a slider 
    ### between 0 - 10 with an interval of 2 and an initial value of your choice
    dcc.Slider(
        min=0,
        max=10,
        step=2,
        value=5
    ),
    ### use the dropdown component from dash core components and set the options to be
    ### a list of your favourite emojis (😏) or your favourite ice cream toppings
    dcc.Dropdown(
        options=[{"label":"😳","value": "ayo sus"},]),
])


# entry point of the application
if __name__ == '__main__':
    app.run_server(debug=True)