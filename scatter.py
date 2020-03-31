#scatter.py
import plotly.graph_objects as go 

xvals = [1, 2, 3, 4, 5, 6, 7, 8]
yvals = [22, 13, 24, 18, 11, 29, 25, 30]

scatter_data = go.Scatter(
  x=xvals, 
  y=yvals, 
  mode='markers',
  marker={'symbol':'star', 'size': 30, 'color': 'magenta'}
)
basic_layout = go.Layout(title="A Scatter(Line) Plot")
fig = go.Figure(data=scatter_data, layout=basic_layout)

fig.write_html("scatter.html", auto_open=True)
