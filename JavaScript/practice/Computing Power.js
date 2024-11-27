function CP(x, n) {
  if (n == 0) return 1;
  temp = CP(x, Math.floor(n / 2));
  temp = temp * temp;
  if (n % 2 == 0) return temp;
  else return temp * x;
}

console.log(CP(3, 5));
console.log(CP(2, 2));
console.log(CP(3, 3));
console.log(CP(5, 3));
console.log(CP(10, 5));
console.log(CP(20, 2));
