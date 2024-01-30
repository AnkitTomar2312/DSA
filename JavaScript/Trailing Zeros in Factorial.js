function findZeros(N) {
  let count = 0;
  let i = 5;
  while (N / i >= 1) {
    count += Math.floor(N / i);
    i *= 5;
  }
  return count;
}

console.log(findZeros(100));
