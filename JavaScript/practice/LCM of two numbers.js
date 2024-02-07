function gcd(a, b) {
  if (b == 0) {
    return a;
  }
  return gcd(b, a % b);
}

function lcm(a, b) {
  return Math.floor((a * b) / gcd(a, b));
}

console.log(lcm(4, 6));
