import pandas as pd

def load_data(file_path):
    # CSV 파일 로드
    data = pd.read_csv(file_path)
    return data

from bokeh.plotting import figure, output_file, show, save
from bokeh.models import ColumnDataSource
from bokeh.layouts import column
import numpy as np

def create_histogram(data, column_name):
    hist, edges = np.histogram(data[column_name], bins=15)
    
    p = figure(title=f"{column_name} Histogram", background_fill_color="#fafafa")
    p.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:], fill_color="blue", line_color="white")

    output_file("histogram.html")
    save(p)  # HTML 파일로 저장
