function evenOdd(l, n) {
  var evenArr = [];
  var oddArr = [];
  for (let i = 0; i < n; i++) {
    if (l[i] % 2 === 0) {
      evenArr.push(l[i]);
    } else {
      oddArr.push(l[i]);
    }
  }
  return { evenArr, oddArr };
}

var l = [10, 20, 30, 40, 50, 60, 71];
var n = l.length;

console.log("Even List: ", evenOdd(l, n).evenArr);
console.log("Odd List: ", evenOdd(l, n).oddArr);
