let names = ['Alice', 'Bob', 'Carol', 'Dave', 'Quandale Dingle'];

for (let name of names) {
    function printName() {
        console.log(name);
    }
    setTimeout(printName, 1000);
}
