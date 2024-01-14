let data = new Set(["ankit", "tomar", "ankit"]);
data.add("kanpur");
data.add({ God: "Krishn" });
console.log(data);
console.log(data.has("ankit"));

// data.clear();
// console.log(data);

// data.delete("ankit");
// console.log(data);

// for (x of data) {
//   console.log(x);
// }

// data.forEach((val) => {
//   console.log(val);
// });

console.log(data.values());
console.log(data.keys());
console.log(data.entries());
