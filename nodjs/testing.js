const readline = require('readline');

let name;

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function askName() {
  return new Promise((resolve, reject) => {
    rl.question('What is your name? ', (input) => {
      name = input;
      rl.close();
      resolve();
    });
  });
}

askName().then(() => {
  console.log(`Hello, ${name}`);
});
setInterval(function(){console.log(name)}, 10)
