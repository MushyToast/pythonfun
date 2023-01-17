var booleanValue: boolean = true;
var counter: number = 0;
while (booleanValue){
    console.log("Hello World");
    counter++;
    console.log(counter);
    let determiner = Math.random();
    if (determiner == 1){
        booleanValue = false;
    }
}