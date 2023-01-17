var booleanValue: boolean = true;
var counter: number = 0;
while (booleanValue){
    console.log("Hello World");
    counter++;
    console.log(counter);
    let determiner = Math.random();
    console.log(determiner + ": determiner")
    if (determiner > 0.95){
        booleanValue = false;
    }
}
console.log("Hello, WOrld!")