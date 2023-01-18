const readLine = require('readline');
const fs = require('fs');
const { string } = require('mathjs');
var age = 0
var name = ""

function writeFile(datal) {
    fs.writeFile('info.txt', datal, (err) => {
        if (err) {
            console.log(err);
        }
    })
}

function getName() {
    return new Promise((resolve, reject) => {
        const rl = readLine.createInterface({
            input: process.stdin,
            output: process.stdout
        });
        rl.question('What is your name? ', (input) => {
            name = input;
            rl.close();
            resolve();
        });
    });
}

function getAge() {
    return new Promise((resolve, reject) => {
        const rl = readLine.createInterface({
            input: process.stdin,
            output: process.stdout
        });
        rl.question('What is your age? ', (input) => {
            age = input;
            rl.close();
            resolve();
        });
    });
}


name = getName()

name.then(() => {
    console.log(`Hello, ${name}`)
    age = getAge()
    age.then(() => {
        console.log(`You are ${age} years old`)
        console.log("Haha! Leaking your info... (This may take a while)")
        const data = `Name: ${name} | Age: ${age}`
        console.log(data)
        setTimeout(console.log("Penis"), 1000)
    })
})