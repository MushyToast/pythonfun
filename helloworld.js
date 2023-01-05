class HelloWorld {
    constructor() {
      this.message = "Hello, World!";
    }
  
    printMessage() {
      console.log(this.message);
    }
  }
  
  const hello = new HelloWorld();
  hello.printMessage();
  