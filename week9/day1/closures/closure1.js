function createCounter() {
  let count = 0; // Private variable
  return function () {
    count++; // Closure accessing the private variable
    return count;
  };
}

// counter has access to the variables in createCounter
const counter = createCounter();
console.log(counter());
console.log(counter());
console.log(counter());
console.log(counter());
