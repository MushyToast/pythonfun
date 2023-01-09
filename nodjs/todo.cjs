const fs = require('fs');
const readline = require('readline');

const intf = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});


function type(text) {
    let index = 0;
  
    function print() {
      if (index < text.length) {
        process.stdout.write(text[index]);
        index++;
        setTimeout(print, 50);
      }
    }
  
    print();
  }
  
type("Welcome to the command line todo list. \n");