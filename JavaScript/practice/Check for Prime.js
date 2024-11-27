function checkPrime(n) {
  if (n == 1) {
    return 1;
  }
  let i = 2;
  while (i * i <= n) {
    if (n % i == 0) {
      return false;
    }
    i++;
  }
  return true;
}

console.log(checkPrime(17));
