const request = require('XMLHttpRequest').XMLHttpRequest;

function getWpData(url) {
  return new Promise((resolve, reject) => {
    var req = new XMLHttpRequest
    req.addEventListener("load", reqListener);
    req.open("GET", "http://www.example.org/example.txt");
    req.send();
    return req
    resolve()
  });
}