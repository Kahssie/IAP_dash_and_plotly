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

df = pd.read_csv("datasets/covid_global.csv")
df_ploting = df.groupby('iso_code', as_index=False)['iso_code', 'new_cases'].tail(1).reset_index()

world_map = go.Figure(
    data=go.Choropleth(
        locations = df_ploting['iso_code'],
        z = df_ploting['new_cases'],
        colorscale = 'Reds',
        hovertemplate = "%{location} - %{z}",
        autocolorscale=False,
        marker_line_color='darkgray',
        marker_line_width=0.5,
        colorbar_title = 'Total Number of cases by country'
    )
)

app.layout = html.Div([
    html.H1("Lets learn callbacks - filtering data from graphs!"),
    html.H3("Covid-19 Cases by country"),
    dcc.Graph(id="world-map", figure = world_map),
    html.Br(),
    dcc.Graph(id="time-series-by-country"),

])


@app.callback(
    Output(component_id='time-series-by-country', component_property='figure'),
    Input(component_id='world-map', component_property='clickData')
)
def update_output_div(clickData):
    if clickData:
        ### print clickdata to see how it is structured
        print(clickData)
        ### then look for the key -> 'location'
        ### write code to retrieve the value of location properly
        selected_country = clickData['points'][0]['location'] 
        df_country = df[df.iso_code == selected_country]
        ### write code to create a plotly scatter plot figure with date as the X-axis and new_cases as the Y-axis 
        fig = px.scatter(df_country, x='date', y='new_cases')
        return fig
    else:
        return {}

if __name__ == '__main__':
    app.run_server(debug=True)
