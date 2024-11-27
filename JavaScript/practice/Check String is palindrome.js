let str = "aaabbbaaa";
function checkPalen(data) {
  let i = 0;
  let j = data.length - 1;
  while (i <= j) {
    if (str[i] !== str[j]) {
      return false;
    }
    i++;
    j--;
  }
  return true;
}

console.log(checkPalen(str));
