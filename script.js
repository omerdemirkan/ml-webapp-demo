const input_button = document.querySelector('#input_button');
const classify_button = document.querySelector('#classify_button');

let file_contents;

input_button.addEventListener('change', function(event) {
  const file = this.files[0];
  const reader = new FileReader();

  reader.addEventListener("load", function(event) {
    file_contents = reader.result.split(',')[1];
  })

  reader.readAsDataURL(file);
});

classify_button.addEventListener('click', function(event) {
  event.preventDefault();

  const body = {
    image: file_contents
  }
  const req = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(body)
  }
  
  fetch('http://127.0.0.1:5000/classify_from_img', req)
    .then(res => res.json())
    .then(console.log);
});



