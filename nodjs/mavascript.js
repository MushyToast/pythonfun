const text = "Hello, World!";

function retrieveText() {
  return new Promise((resolve, reject) => {
    if (text) {
      setTimeout(() => {
        resolve(text);
      }, Math.random() * 5000);
    }
  });
};

async function processText() {
  const text = await retrieveText();
  console.log(text);
};

processText();
