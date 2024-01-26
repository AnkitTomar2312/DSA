const readline = require("node:readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});
readline.question(`Enter the number: ?`, (x) => {
  x = eval(x);
  let sum = (x * (x + 1)) / 2;
  console.log(sum);
  readline.close();
});
