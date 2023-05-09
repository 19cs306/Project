import plotly.graph_objs as go
import os
import plotly.io as pio
import pandas as pd

if os.path.exists('media/India.csv'):
    df = pd.read_csv('media/India.csv')

line1_trace = go.Scatter(x=df['Day'], y=df['CumConfirmed'], mode='lines', name='Confirmed')
line2_trace = go.Scatter(x=df['Day'], y=df['CumDeaths'], mode='lines', name='Deaths')
line3_trace = go.Scatter(x=df['Day'], y=df['CumRecovered'], mode='lines', name='Recovered')


# create the Plotly layout object
layout = go.Layout(title='My Line Graph', xaxis=dict(title='Day'), yaxis=dict(title='Value'))

# create the Plotly figure object
fig = go.Figure(data=[line1_trace, line2_trace, line3_trace], layout=layout)

# show the Plotly figure
pio.write_html(fig, 'media/covid_data.html')