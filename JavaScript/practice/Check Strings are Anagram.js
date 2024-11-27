let str1 = "cat";
let str2 = "act";

function checkAnagram(str1, str2) {
  let ObjStr = {};
  if (str1.length != str2.length) {
    return false;
  }
  for (ch of str1) {
    ObjStr[ch] = (ObjStr[ch] || 0) + 1;
  }
  for (ch of str2) {
    if (!ObjStr[ch]) {
      return false;
    }
    ObjStr[ch]--;
  }
  return true;
}

console.log(checkAnagram(str1, str2));
