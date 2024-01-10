let array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
let solution = [];
let counter = 0;
for (let i = 0; i < array.length; i++) {
  if (array[i] % 2 == 0) {
    solution.push(array[i] * 2);
    counter++;
  }
}

console.log(
  "The solution is " + solution + " The length of solution is " + counter
);
