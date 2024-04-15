from bokeh.plotting import figure, curdoc
from bokeh.embed import server_document
from bokeh.models import ColumnDataSource
from bokeh.layouts import column
import numpy as np

# Generate some data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a Bokeh plot
source = ColumnDataSource(data=dict(x=x, y=y))
plot = figure(title="Bokeh Plot", plot_width=400, plot_height=400)
plot.line('x', 'y', source=source, line_width=2)

# Add the plot to the current document (required for Bokeh server)
curdoc().add_root(column(plot))
