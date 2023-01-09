const fs = require('fs');
const readline = require('readline');

const intf = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});


const text = "Hello, World!";
let index = 0;

function type() {
  if (index < text.length) {
    process.stdout.write(text[index]);
    index++;
    setTimeout(type, 50);
  }
}

type();
