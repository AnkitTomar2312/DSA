function AdditionUnderModulo(a, b) {
  let x = 10;
  let n = 9;
  let res = 1;
  while (n > 0) {
    if (n % 2 !== 0) {
      res = res * x;
    }
    x = x * x;
    n = Math.floor(n / 2);
  }
  return BigInt(a + b) % BigInt(res + 7);
}

console.log(AdditionUnderModulo(9223372036854775807, 9223372036854775807));
