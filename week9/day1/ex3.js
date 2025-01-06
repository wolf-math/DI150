// Analyse this code before executing it. Write explanatory comments. What will be the output ?

// parent function
function add() {
  // block scope variable
  let counter = 0;
  // child function
  function plus() {
    // accessing block scoped variable
    // increment by 1
    counter += 1;
    // log to console.
    console.log(counter);
  }
  // invoke the plus function
  plus();
}

// invokes the add function
add();
add();
add();
add();
