let data = {
  name: "Ankit",
  age: 21,
  mail: "ankitjdec@gmail.com",
  getName: function () {
    return this.name;
  },
};

data.car = "Ferrari";
delete data.age;

console.log(Object.keys(data));
console.log(Object.values(data));
console.log(Object.entries(data));
