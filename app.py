from flask import Flask, request, jsonify, render_template, redirect, url_for
from werkzeug.utils import secure_filename
import os
import pandas as pd
from bokeh.plotting import figure, output_file, save
from bokeh.models import ColumnDataSource
from bokeh.layouts import column
import numpy as np
from bokeh.plotting import figure, show

# Flask 인스턴스 설정
app = Flask(__name__, static_url_path='', static_folder='static')
app.config['UPLOAD_FOLDER'] = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'csv'}  # 이 변수를 전역으로 정의

# 파일이 허용되는 형식인지 확인하는 함수
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# 메인 페이지 라우트
@app.route('/')
def index():
    return render_template('index.html')

# 파일 업로드를 위한 라우트
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "There is no file"}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "There is no such file name"}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        try:
            data = pd.read_csv(file_path, delimiter=',', encoding='utf-8', on_bad_lines='skip')
            histogram_script = process_and_create_histogram(data)
            return render_template('display_histogram.html', script=histogram_script)
        except Exception as e:
            return jsonify({"error": f"error uploading file: {e}"}), 500





def process_and_create_histogram(file_path):
    # 데이터 불러오기
    data = pd.read_csv(file_path, header=None)


    # 데이터 검사 및 전처리
    print(data.head())  # 데이터 확인
    data.info()         # 데이터 정보 확인
    data.describe()     # 통계 정보 확인
    
    # 필요한 열만 선택
    data = data[['distance', 'mass']]  # 가정: 'distance'와 'mass' 열이 필요하다고 가정
    
    # 결측치 처리
    data = data.dropna()  # 결측치가 있는 행을 제거

    # 데이터 타입 변환
    data['distance'] = data['distance'].astype(float)
    data['mass'] = data['mass'].astype(float)

    # 데이터 정제 후 히스토그램 생성
    histogram_script = process_and_create_histogram(data, 'distance')
    return histogram_script


if __name__ == '__main__':
    app.run(debug=True)
