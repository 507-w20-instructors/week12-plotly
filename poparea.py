#cities.py

import plotly.graph_objects as go 

cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
population = [ 8398748, 3990456, 2705994, 2325502, 1660272]
area = [301.5, 468.7, 227.3, 637.5, 517.6]

scatter_data = go.Scatter(
    x=area, 
    y=population,
    text=cities, 
    marker={'symbol':'square', 'size':30, 'color': 'green'},
    mode='markers')
basic_layout = go.Layout(title="US Cities Area vs Population")
fig = go.Figure(data=scatter_data, layout=basic_layout)

fig.write_html("poparea.html", auto_open=True)
