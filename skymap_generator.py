from bokeh.plotting import figure, output_file, show
from bokeh.tile_providers import get_provider
from astropy.coordinates import SkyCoord
import numpy as np

# Sample data for demonstration (replace this with your actual data)
n_galaxies = 1000
gxy_ra = np.random.uniform(0, 360, n_galaxies)
gxy_dec = np.random.uniform(-90, 90, n_galaxies)

# Convert RA and Dec to Web Mercator coordinates for plotting on Bokeh tile map
def ra_dec_to_web_mercator(ra, dec):
    ra_rad = np.radians(ra)
    dec_rad = np.radians(dec)
    x = ra_rad * 6378137.0
    y = np.log(np.tan((np.pi / 4) + (dec_rad / 2))) * 6378137.0
    return x, y

# Convert RA and Dec to Web Mercator coordinates
x, y = ra_dec_to_web_mercator(gxy_ra, gxy_dec)

# Output to HTML file
output_file("skymap.html")

# Create figure with OpenStreetMap tile provider
tile_provider = get_provider('OSM')
p = figure(title="Skymap", plot_width=800, plot_height=600, x_range=(-20000000, 20000000), y_range=(-20000000, 20000000),
           x_axis_type="mercator", y_axis_type="mercator")
p.add_tile(tile_provider)

# Plot galaxies on the skymap
p.circle(x=x, y=y, size=5, color="blue", alpha=0.6)

# Show the plot
show(p)
