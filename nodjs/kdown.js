const readLine = require('readline');
const fs = require('fs');

const rl = readLine.createInterface({
    input: process.stdin,
    output: process.stdout
  });
var age = 0
var name = ""
rl.question("How old are you?\n", (input) =>{
    age = input
    console.log("You are " + input + " years old!")
    rl.close();
})

const rl1 = readLine.createInterface({
    input: process.stdin,
    output: process.stdout
  });

rl1.question("What is your full name?\n", (input) =>{
    name = input
    console.log("Your name is " + input + "!")
    rl.close();
})