const https = require('https')

function getWpData(url) {
  return new Promise((resolve, reject) => {
    const options = {
      hostname: url,
      port: 443,
      path: '/index.html',
    }
    
  });
}