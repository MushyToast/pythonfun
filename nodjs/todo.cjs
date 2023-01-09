const fs = require('fs');
const readline = require('readline');

const intf = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});


function* getKeystroke() {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });

  // Yield the code here until a key is pressed
  const key = yield new Promise(resolve => rl.once('line', resolve));

  // Close the readline interface
  rl.close();

  // Return the key that was pressed
  return key;
}

const generator = getKeystroke();

// Start the generator and get the promise that is returned
const keyPromise = generator.next().value;

// Wait for the key to be pressed and then log it to the console
keyPromise.then(key => {
  console.log(key);
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
var key = await getKeystroke()
console.log(key)