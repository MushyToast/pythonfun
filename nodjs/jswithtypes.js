var test = 0;
function e() {
    new Promise(function (resolve, reject) {
        return resolve(0);
    });
}
console.log(e());
