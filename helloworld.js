((() => {
    const message = "Hello, World!";
  
    const printMessage = () => {
      console.log(message);
    };
  
    const delay = (ms) => {
      return new Promise((resolve) => {
        setTimeout(resolve, ms);
      });
    };
  
    const printWithDelay = async (delayTime) => {
      await delay(delayTime);
      printMessage();
    };
  
    const delays = [1000, 2000, 3000, 4000, 5000];
    const printAll = async () => {
      for (const delayTime of delays) {
        await printWithDelay(delayTime);
      }
    };
  
    const runNTimes = async (n) => {
      for (let i = 0; i < n; i++) {
        await printAll();
      }
    };
  
    runNTimes(5);
  }))();