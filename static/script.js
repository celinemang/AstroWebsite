document.addEventListener("DOMContentLoaded", function() {
  const uploadForm = document.getElementById('uploadForm'); // HTML 내 form의 id 가정

  uploadForm.addEventListener('submit', function(event) {
      event.preventDefault(); // 폼의 기본 제출 동작을 막음

      const formData = new FormData(uploadForm);
      fetch('/upload', {
          method: 'POST',
          body: formData,
      })
      .then(response => response.json()) // 응답을 JSON 형식으로 파싱
      .then(data => {
          console.log('Success:', data);
          // 성공적으로 데이터를 전송하고 서버로부터 응답을 받으면 여기에서 처리
      })
      .catch((error) => {
          console.error('Error:', error);
          // 오류 처리
      });
  });
});
