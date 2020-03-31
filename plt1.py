import plotly.graph_objs as go 

xvals = ['foo', 'bar', 'baz']
yvals = [5, 4, 6]

bar_data = go.Bar(x=xvals, y=yvals)
basic_layout = go.Layout(title="A Bar Graph")
fig = go.Figure(data=bar_data, layout=basic_layout)

fig.show()


