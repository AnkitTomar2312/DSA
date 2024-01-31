// function gcd(a, b) {
//   while (a !== b) {
//     if (a > b) {
//       a = a - b;
//     } else {
//       b = b - a;
//     }
//   }
//   return a;
// }

// console.log(gcd(10, 15));

//OPTIMIZED APPROACH
function GCD(a, b) {
  if (b === 0) {
    return a;
  }
  return GCD(b, a % b);
}

console.log(GCD(10, 15));
