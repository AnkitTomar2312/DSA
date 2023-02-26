function printDivisor(n) {
  var i = 0;
  while (i * i < n) {
    if (n % i == 0) {
      console.log(i);
    }
    i += 1;
  }
  while (i >= 1) {
    if (n % i == 0) {
      console.log(Number(n / i));
    }
    i -= 1;
  }
}

printDivisor(12);
