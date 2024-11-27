const readline = require("node:readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});
readline.question(`Enter number you want to check: `, (val) => {
  let temp = Number(val);
  let rev = 0;
  while (temp > 0) {
    let ld = temp % 10;
    rev = rev * 10 + ld;
    temp = Math.floor(temp / 10);
  }
  if (rev == val) {
    console.log("True");
  } else {
    console.log("False");
  }
  readline.close();
});
