const getSmallerNumber = (l, n, num) => {
  var sl = [];
  for (let i = 0; i < n; i++) {
    if (l[i] < num) {
      sl.push(l[i]);
    }
  }
  return sl;
};

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
num = 7;
n = l.length;
console.log(getSmallerNumber(l, n, num));
