const readLine = require('readline');
const fs = require('fs');
var age = 0
var name = ""
function getName() {
    const rl = readLine.createInterface({
        input: process.stdin,
        output: process.stdout
    });
    rl.question("What is your name? ", function (answer) {
        name = answer
        rl.close()
    });
    return name
}

name = getName()

console.log("Welcome,", name)