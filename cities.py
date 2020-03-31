#cities.py

import plotly.graph_objects as go 

cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
population = [ 8398748, 3990456, 2705994, 2325502, 1660272]

bar_data = go.Bar(x=cities, y=population)
basic_layout = go.Layout(title="US Cities by Population")
fig = go.Figure(data=bar_data, layout=basic_layout)

fig.show()
