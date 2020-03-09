const file_input = document.querySelector('#file-input');
const text_input = document.querySelector('#text-input');
const browse_button = document.querySelector('#browse-button');
const preview = document.querySelector('#preview');
const classify_button = document.querySelector('#classify-button');
const output_header = document.querySelector("#output-header");

let file_contents;

browse_button.addEventListener('click', function(event) {
  file_input.click();
})

// reads base64 byte-string encoding of image into file_contents
file_input.addEventListener('change', function(event) {
  const file = this.files[0];
  const reader = new FileReader();
  text_input.value = file.name;

  reader.addEventListener("load", function(event) {
    file_contents = reader.result.split(',')[1];
    preview.src = reader.result;
  })
  reader.readAsDataURL(file);

  output_header.innerText = '';
});

classify_button.addEventListener('click', function(event) {
  if (file_contents == null) return;

  // creating request
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
  
  // sending request and displaying response
  fetch('http://127.0.0.1:5000/classify_from_img', req)
    .then(res => res.json())
    .then((res) => {
      let confidence;
      if(res['animal'] === 'cat') {
        confidence = (parseFloat(res['activation'])*100).toFixed(2);
      } else {
        confidence = ((1 - parseFloat(res['activation']))*100).toFixed(2);
      }

      output_header.innerText = `
          The model predicted "${res['animal']}"
          with ${confidence}% confidence.
        `;
    });
});



