const readline = require('readline');

let name;

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

async function askName() {
  return new Promise((resolve, reject) => {
    rl.question('What is your name? ', (input) => {
      name = input;
      rl.close();
      resolve();
    });
  });
}

(async function() {
  await askName();
  console.log(`Hello, ${name}`);
  for (let i = 0; i < name.length; i++) {
  console.log(name[i], "\r");
}
})();