function abc() {
  return "Start of Netflix";
}

function xyz() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve("Watch NetFlix");
    }, 3000);
  });
}

function prq() {
  return "Close NetFlix";
}

var callAll = async () => {
  console.log(abc());
  console.log(await xyz());
  console.log(prq());
};

callAll();
