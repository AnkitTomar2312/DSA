function AllDiv(n) {
  let i = 1;
  while (i * i <= n) {
    if (n % i == 0) {
      console.log(i);
    }
    i++;
  }
  while (i >= 1) {
    if (n % i == 0) {
      console.log(n / i);
    }
    i--;
  }
}

console.log(AllDiv(17));
