var readLine = require('readline');
var fs = require('fs');
var string = require('mathjs').string;
var age = 0;
var name = "";
function writeFile(datal) {
    fs.writeFile('info.txt', datal, function (err) {
        if (err) {
            console.log(err);
        }
        console.log("Done! Your info has been leaked! Enjoy being doxxed!");
    });
}
function getName() {
    return new Promise(function (resolve, reject) {
        var rl = readLine.createInterface({
            input: process.stdin,
            output: process.stdout
        });
        rl.question('What is your name? ', function (input) {
            name = input;
            rl.close();
            resolve();
        });
    });
}
function getAge() {
    return new Promise(function (resolve, reject) {
        var rl = readLine.createInterface({
            input: process.stdin,
            output: process.stdout
        });
        rl.question('What is your age? ', function (input) {
            age = input;
            rl.close();
            resolve();
        });
    });
}
name = getName();
name.then(function () {
    console.log("Hello, ".concat(name));
    age = getAge();
    age.then(function () {
        console.log("You are ".concat(age, " years old"));
        console.log("Haha! Leaking your info... (This may take a while)");
        var data = "Name: ".concat(name, " | Age: ").concat(age);
        setTimeout(function () {
            writeFile(data);
        }, 10000);
    });
});

console.log("Hello,");