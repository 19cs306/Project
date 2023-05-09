import plotly.graph_objs as go
from sklearn.linear_model import LinearRegression
import pandas as pd
import plotly.io as pio
import os

if os.path.exists('media/India.csv'):
    df = pd.read_csv('media/India.csv')

def train_model(df):
    X = [[x] for x in df['Day']]
    y = df['CumConfirmed']
    # define the hyperparameter grid
    param_grid = {'copy_X': True, 'fit_intercept': False, 'n_jobs': 1, 'positive': True}
    model = LinearRegression(**param_grid)
    model.fit(X, y)
    return model

def make_pred(day_num):
    model = train_model(df)
    predicted_cases = model.predict([[day_num]])
    return int(predicted_cases)

# create a trace for the actual data
trace_actual = go.Scatter(
    x=df['Day'],
    y=df['CumConfirmed'],
    name='Actual Data'
)

# create a trace for the linear regression line
x_range = [0, max(df['Day'])]
y_range = [make_pred(0), make_pred(max(df['Day']))]
trace_regression = go.Scatter(
    x=x_range,
    y=y_range,
    name='Linear Regression Line'
)

# create the layout for the graph
layout = go.Layout(
    title='Linear Regression Model Evaluation',
    xaxis=dict(title='Day'),
    yaxis=dict(title='Cumulative Confirmed Cases')
)

# create the figure and add the traces and layout
fig = go.Figure(data=[trace_actual, trace_regression], layout=layout)
# display the figure
pio.write_html(fig, 'media/covid_model.html')
