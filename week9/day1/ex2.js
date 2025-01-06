// scope

// function checkAge(age) {
//   let message;
//   if (age < 18) {
//     message = "Sorry, you're too young.";
//   } else {
//     message = "Yay! You're old enough!";
//   }

//   return message;
// }

// console.log(checkAge(21));

// scope

// function numbers() {
//   for (let i = 0; i < 5; i += 1) {
//     console.log(i);
//   }
//   console.log(i);
// }
// numbers();

// ternary operator

// function checkHunger(hungry = true) {
//   return hungry ? 'look in the fridge' : 'do coding exercises';
// }

// console.log(checkHunger(true));
// console.log(checkHunger(false));

// Create a function to check the year given by the user

// If the year is after 2000, you should display "You are in the 21st century", else you should display "You live in the Middle Age"

function checkYear(year) {
  return year > 2000
    ? 'You are in the 21st century'
    : 'You live in the Middle Ages';
}

console.log(checkYear(1980));
console.log(checkYear(2011));
console.log(checkYear(9000));
