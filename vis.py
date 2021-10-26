import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# Import and clean data (importing csv into pandas)
# dataframe variable
df = pd.read_csv("_______")

df = df.groupby([])[[]].