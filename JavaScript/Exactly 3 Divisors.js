function isPrime(n) {
  if (n <= 1) return false;
  if (n <= 3) return true;
  if (n % 2 === 0 || n % 3 === 0) return false;
  for (let i = 5; i * i <= n; i = i + 6) {
    if (n % i === 0 || n % (i + 2) === 0) return false;
  }
  return true;
}

let N = 6;
let count = 0;
for (let i = 2; i * i <= N; i++) {
  if (isPrime(i)) {
    let val = i * i;
    if (val <= N) count++;
  }
}
console.log(count);
