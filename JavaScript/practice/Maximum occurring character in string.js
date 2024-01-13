let spacestr =
  "hello my name is ankit tomar i am a webdeveloper nice to meet you";
let str = spacestr.replace(/\s/g, "");
let Obj = {};
let max = "";
// for (ch of str) {
//   Obj[ch] = (Obj[ch] || 0) + 1;
// }

for (let i = 0; i < str.length; i++) {
  key = str[i];
  if (!Obj[key]) {
    Obj[key] = 0;
  }
  Obj[key]++;
  if (max == "" || Obj[key] > Obj[max]) {
    max = key;
  }
}

console.log(Obj, max);
