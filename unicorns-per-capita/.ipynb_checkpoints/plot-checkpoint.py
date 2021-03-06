import pandas as pd
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

plotly.offline.init_notebook_mode(connected=True)
import plotly.io as pio
import os

def make_plot(x, z):
    data = [go.Choropleth(
        locations = x,
        z = z,
        text = x,
        locationmode="country names",
        autocolorscale = True,
        marker = go.choropleth.Marker(
            line = go.choropleth.marker.Line(
                color = 'rgb(0,0,0)',
                width = 0.5
            )),
        colorbar = go.choropleth.ColorBar(
            len=0.5
        ),
    )]

    layout = go.Layout(
        height=700,
        width=700,
        margin={"t": 0, "b": 0, "l": 0, "r": 0},
        geo = go.layout.Geo(
            showframe = True,
            showcoastlines = True,
            showcountries = True,
            projection = go.layout.geo.Projection(
                type = 'mercator'
            )
        )
    )

    fig = go.Figure(data = data, layout = layout)
    iplot(fig)