function InterativePower(x, n) {
  let res = 1;
  while (n > 0) {
    if (n % 2 !== 0) {
      res = res * x;
    }
    x = x * x;
    n = Math.floor(n / 2);
  }
  return res;
}

console.log(InterativePower(4, 5));
