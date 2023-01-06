const http = require('https');
const fs = require('fs');
const url = 'https://mushytoast.github.io/';

http.get(url, (response) => {
  let data = '';

  response.on('data', (chunk) => {
    data += chunk;
  });

  response.on('end', () => {
    fs.writeFile(
        'export.html',
        data
    )
  });
}).on('error', (error) => {
  console.error(error);
});
