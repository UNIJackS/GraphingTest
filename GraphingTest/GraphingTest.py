from pandas import DataFrame
import plotly.express as px
import pandas as pd

fileName = "IAT.csv"


df = pd.read_csv(fileName)

fig = px.box(df, y="Value",points="all")
fig.show()

print("test")