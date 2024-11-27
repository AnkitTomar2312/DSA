function PF(n) {
  for (let i = 2; i <= n + 1; i++) {
    if (isPrime(i)) {
      let x = i;
      while (n % x == 0) {
        console.log(i);
        x = i * x; //checking for that number divide repeat
      }
    }
  }
}

function isPrime(n) {
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

console.log(PF(90));
