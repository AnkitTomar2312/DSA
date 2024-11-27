let array = [];
for (let i = 100; i > 0; i--) {
  array.push(i);
}
function InsertionSort(data) {
  let i, j, current;
  for (i = 1; i < data.length; i++) {
    current = data[i];
    j = i - 1;
    while (j >= 0 && data[j] > current) {
      data[j + 1] = data[j];
      j--;
    }
    data[j + 1] = current;
  }
}

InsertionSort(array);
console.log(array);
