const counter = (function () {
  let count = 0; // Private variable
  return function () {
    count++;
    return count;
  };
})();

console.log(counter()); // 1
console.log(counter()); // 2
console.log(counter()); // 3
