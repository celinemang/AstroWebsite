const multer = require('multer');
const express = require('express');
const fs = require('fs');
const path = require('path');
const app = express();
const PORT = 3000;

// 정적 파일 제공을 위한 미들웨어 추가
app.use(express.static(path.join(__dirname, 'static')));

// 사용자 정의 스토리지 엔진 설정
const storage = multer.diskStorage({
  destination: function(req, file, cb) {
    cb(null, 'uploads/'); // 파일이 저장될 서버 상의 경로
  },
  filename: function(req, file, cb) {
    // 파일 이름 설정: 필드명-타임스탬프.확장자
    cb(null, file.fieldname + '-' + Date.now() + path.extname(file.originalname));
  }
});

// storage 설정을 사용해 multer 인스턴스 생성
const upload = multer({ storage: storage }); // multer에 storage 설정을 전달합니다.

// 파일 업로드를 위한 라우트 설정
app.post('/upload', upload.single('file'), (req, res) => {
  if (req.file) {
    console.log(`File uploaded: ${req.file.originalname}`);
    res.status(200).json({ message: 'File uploaded successfully.' }); // 성공 메시지를 담은 JSON 응답을 보냅니다.
  } else {
    res.status(400).json({ message: 'No file uploaded.' }); // 파일이 업로드되지 않았을 때 오류 메시지를 보냅니다.
  }
});

// 서버를 시작합니다.
app.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}`);
});

//new 

document.getElementById('uploadForm').addEventListener('submit', function(e) {
  e.preventDefault();  // 폼 기본 제출 동작을 방지
  var formData = new FormData(this);  // 폼 데이터를 FormData 객체로 생성
  fetch('/upload', {
      method: 'POST',
      body: formData
  })
  .then(response => response.json())  // 응답을 JSON 형태로 파싱
  .then(data => {
      if (data.error) {
          alert(data.error);  // 오류가 있을 경우 경고
      } else {
          displayData(data.data);  // 데이터를 화면에 표시하는 함수 호출
      }
  })
  .catch(error => console.error('Error:', error));
});

function displayData(data) {
  const output = document.getElementById('output');
  output.innerHTML = '';  // 출력 영역을 초기화
  data.forEach(item => {
      const p = document.createElement('p');
      p.textContent = item.join(' ');  // 배열을 문자열로 변환하여 표시
      output.appendChild(p);
  });
}
