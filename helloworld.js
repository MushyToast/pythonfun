let names = ['Alice', 'Bob', 'Carol', 'Dave', 'Quandale Dingle'];

function wait(time) {
    function empty() {}
    setTimeout(empty, time)
}


wait(100000);
console.log(names[0]);