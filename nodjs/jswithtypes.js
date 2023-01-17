var booleanValue = true;
var counter = 0;
while (booleanValue) {
    console.log("Hello World");
    counter++;
    console.log(counter);
    var determiner = Math.random();
    console.log(determiner + ": determiner");
    if (determiner > 0.95) {
        booleanValue = false;
    }
}
