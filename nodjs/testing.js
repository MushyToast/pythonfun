const https = require('https');

function getWpData(url) {
  return new Promise((resolve, reject) => {
    const options = {
      hostname: url,
      port: 443,
      path: '/index.html',
    }
    https.get(options, function(res){
      res.on('data', function(d) {
        return d
        resolve(d);
      });
      res.on('error', function(e){
        return e
        reject(e);
      });
    });
  });
}

req = getWpData('www.google.com');

req.on('resolve', function(data){
  console.log(data);
});