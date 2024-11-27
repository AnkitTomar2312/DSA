function quadraticRoots(a, b, c) {
  let D = b * b - 4 * a * c;
  console.log(D);
  if (D > 0) {
    let root1 = Math.floor((-b + Math.sqrt(D)) / (2 * a));
    let root2 = Math.floor((-b - Math.sqrt(D)) / (2 * a));
    return [Math.max(root1, root2), Math.min(root1, root2)];
  } else if (D === 0) {
    root = Math.floor(-b / (2 * a));
    return [root, root];
  } else {
    return ["Complex root", "complex root"];
  }
}

console.log(quadraticRoots(752, 904, 164));
