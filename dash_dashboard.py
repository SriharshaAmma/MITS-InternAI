import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

def init_dashboard(server):
    app = dash.Dash(__name__, server=server, routes_pathname_prefix='/dashboard/')
    df = pd.read_csv('data/engagement.csv')

    fig = px.bar(df, x='Domain', y='Applications', title='Internship Applications by Domain')

    app.layout = html.Div([
        html.H1("MITS Internship Dashboard"),
        dcc.Graph(figure=fig)
    ])
