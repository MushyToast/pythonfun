const fs = require('fs');
const readline = require('readline');

const intf = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function getkey() {
  var stdin = process.stdin;

// without this, we would only get streams once enter is pressed
  stdin.setRawMode( true );

// resume stdin in the parent process (node app won't quit all by itself
// unless an error or process.exit() happens)
  stdin.resume();

// i don't want binary, do you?
  stdin.setEncoding( 'utf8' );

// on any data into stdin
  stdin.on( 'data', function( key ){
  // ctrl-c ( end of text )
  if ( key === '\u0003' ) {
    process.exit();
  }
  return key
});
}

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
console.log(getkey())
