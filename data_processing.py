import numpy as np
import pandas as pd
from bokeh.plotting import figure
from bokeh.embed import components
import matplotlib.pyplot as plt

def load_and_process_data(filepath):
    distances = []
    masses = []
    with open(filepath, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) >= 5:
                try:
                    dist = float(parts[1])
                    mass = float(parts[2])
                    distances.append(dist)
                    masses.append(mass)
                except ValueError:
                    continue
    
    return np.array(distances), np.array(masses)

def create_histogram(distances):
    plt.figure(figsize=(10, 6))
    plt.hist(distances, bins=30, color='skyblue', edgecolor='black')
    plt.title('Distribution of Galaxy Distances')
    plt.xlabel('Distance (Mpc)')
    plt.ylabel('Frequency')
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.savefig('static/histogram.png')
    plt.close()
    return 'static/histogram.png'

def create_bokeh_plot(masses):
    p = figure(title="Mass Distribution", x_axis_label='Mass', y_axis_label='Number')
    p.line(range(len(masses)), masses, line_width=2)
    script, div = components(p)
    return script, div
