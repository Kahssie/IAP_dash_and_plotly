from dash import Dash, callback, Input, Output, callback_context, html, dcc
import plotly.express as px
import plotly.graph_objects as go

app = Dash(__name__)

app.layout = html.Div([
    html.Button('Draw Graph', id='draw'),
    html.Button('Reset Graph', id='reset'),
    dcc.Graph(id='graph')
])

@app.callback(
    Output('graph', 'figure'),
    Input('reset', 'n_clicks'),
    Input('draw', 'n_clicks'),
    prevent_initial_call=True
)
def update_graph(b1, b2):
    triggered_id = callback_context.triggered[0]['prop_id']
    if 'reset.n_clicks' == triggered_id:
         return reset_graph()
    elif 'draw.n_clicks' == triggered_id:
         return draw_graph()

def draw_graph():
    df = px.data.iris()
    return px.scatter(df, x=df.columns[0], y=df.columns[1])

def reset_graph():
    return go.Figure()

if '__name__' == "__main__":
    app.run_server(debug=True)