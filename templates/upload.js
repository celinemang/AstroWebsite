document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('uploadForm'); // Form ID 수정 필요
    form.addEventListener('submit', function(e) {
      e.preventDefault();
      const formData = new FormData(form);
      fetch('/upload', {
          method: 'POST',
          body: formData,
      })
      .then(response => response.json())
      .then(data => {
          alert(data.message); // 성공 메시지를 알림으로 표시
          // 예: document.getElementById('uploadResult').innerText = data.message;
      })
      .catch(error => {
          console.error('Error:', error);
          alert('File upload failed.');
      });
  });
  });
  