let array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 3, 9, 4];
let key = 0;
for (let i = 0; i < array.length; i++) {
  key = array[i];
  for (let j = i + 1; j < array.length; j++) {
    if (key === array[j]) {
      console.log(key);
    }
  }
}
