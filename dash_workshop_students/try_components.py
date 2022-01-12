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
fig = None


# The layout holds all the components of your app
# Everything is in one html div Component
app.layout = html.Div(children=[
    ### use some html header (H1-6)

    ### use a html break to leave some space

    ### use a html div to give a description of your app (or just put your name)

    ### use the graph component from dash core components to display the graph from above (fig)

    ### use the slider component from dash core components to make a slider 
    ### between 0 - 10 with an interval of 2 and an initial value of your choice

    ### use the dropdown component from dash core components and set the options to be
    ### a list of your favourite emojis (😏) or your favourite ice cream toppings
])


# entry point of the application
if __name__ == '__main__':
    app.run_server(debug=True)