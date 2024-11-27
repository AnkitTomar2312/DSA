const readline = require("node:readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});
readline.question(`enter the number: `, (n) => {
  let x = Number(n);
  let counter = 0;
  while (x > 0) {
    x = Math.floor(x / 10);
    counter++;
  }
  readline.close();
  console.log(counter);
});
