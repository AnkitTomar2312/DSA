//{name=>Ankit}
//In map we can use any data type
let data = new Map([
  ["name", "ankit"],
  [true, "bool key"],
  [100, "hundred"],
]);

data.set("color", "green");
// console.log(data.size);
// console.log(data.has(100));
// console.log(data.get(100));
// data.clear();

// for (x of data) {
//   console.log(x);
// }

// data.forEach((val, key) => {
//   console.log(key);
// });

data.delete("name");

console.log(data);
// How i can insert value in map dynamically
