const readline = require('readline');

let name;

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

async function askName() {
    await rl.question('What is your name? ', (input) => {
        name = input;
        rl.close();
      });
}

rl.on('close', () => {
  console.log(`Hello, ${name}`);
});

setInterval(function(){console.log(name)},)