function DigitsInFactorial(N) {
  if (N < 0) return 0;
  if (N < 1) return 1;
  let digitCounter = 0;
  for (let i = 2; i <= N; i++) {
    digitCounter += Math.log10(i);
  }
  return Math.floor(digitCounter + 1);
}

console.log(DigitsInFactorial(5));
