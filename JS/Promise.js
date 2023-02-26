//crating a promise
function abc(value) {
  return new Promise((resolve, reject) => {
    if (value < 12) {
      resolve("It's Done");
    } else {
      reject("It's not done");
    }
  });
}

//calling for a promise
abc(12)
  .then((data) => {
    console.log(data);
  })
  .catch((e) => {
    console.log(e);
  });
