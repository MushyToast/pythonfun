const readLine = require('readline');
const fs = require('fs');

const rl = readLine.createInterface({
    input: process.stdin,
    output: process.stdout
  });

rl.question("How old are you?\n", (age) =>{
    console.log("You are " + age + " years old!")
    rl.close();
})
