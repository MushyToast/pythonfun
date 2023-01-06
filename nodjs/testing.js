const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});


var username = rl.question('What is your name? ', (name) => {
  console.log(`Hello, ${name}`);
  rl.close();
  return name
});

console.log(username)