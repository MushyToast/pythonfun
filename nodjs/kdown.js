const readLine = require('readline');
const fs = require('fs');
var age = 0
var name = ""

//create a function that asks for the users name, and returns it in promise form so it wont run until the user has inputted their name
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
})

name.then(() => {
    age = getAge()
    age.then(() => {
        console.log(`You are ${age} years old`)
    })
    setTimeout()
})