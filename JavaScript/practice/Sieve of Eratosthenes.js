function SoF(n) {
  if (n <= 1) {
    return;
  }
  let arr = new Array(n + 1).fill(true);
  let i = 2;
  while (i <= n) {
    if (arr[i]) {
      console.log(i);
    }
    for (let j = i * i; j <= n; j += i) {
      arr[j] = false;
    }
    i++;
  }
}

SoF(10);
