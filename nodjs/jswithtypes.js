var booleanValue = true;
var counter = 0;
while (booleanValue) {
    console.log("Hello World");
    counter++;
    console.log(counter);
    var determiner = Math.random();
    if (determiner == 1) {
        booleanValue = false;
    }
}
