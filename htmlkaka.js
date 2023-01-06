const http = require('https');

const url = 'https://mushytoast.github.io/';

http.get(url, (response) => {
  let data = '';

  response.on('data', (chunk) => {
    data += chunk;
  });

  response.on('end', () => {
    console.log(data);
  });
}).on('error', (error) => {
  console.error(error);
});
