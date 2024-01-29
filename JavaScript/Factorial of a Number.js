//ITERATUVE APPROACH:-

// let num = 5;
// let res = 1;
// for (let i = 2; i <= num; i++) {
//   res = res * i;
// }
// console.log(res);

//RECURSIVE APPROACH:-

let num = 10;
function Fact(num) {
  if (num == 0) {
    return 1;
  }
  return num * Fact(num - 1);
}

console.log(Fact(num));
