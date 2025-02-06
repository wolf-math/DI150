// 🌟 Exercise 2 : Colors #2
// Instructions
// Using these arrays :

const colors = ['Blue', 'Green', 'Red', 'Orange', 'Violet', 'Indigo', 'Yellow'];

// Write a JavaScript program that displays the colors in the following order : “1st choice is Blue .” “2nd choice is Green.” “3rd choice is Red.” ect…
// Hint : Use the array methods taught in class and ternary operator.

const suffixer = (num) => {
  const ordinal = ['th', 'st', 'nd', 'rd'];
  // 1 = st
  // 2 = nd
  // 3 = rd
  // 4-10 = th

  return num % 10 === 1
    ? `${num}st`
    : num % 10 === 2
    ? `${num}nd`
    : num % 10 === 3
    ? `${num}rd`
    : `${num}th`;
};

(function () {
  colors.forEach((color, index) =>
    console.log(`${suffixer(index + 1)} choice is ${color}`)
  );
})();
