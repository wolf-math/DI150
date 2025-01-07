// FOREACH

// const myArr = [3, 4, 5, 6, 7, 8, 9];

// for (let i of myArr) {
//   console.log(i);
// }

// myArr.forEach((number, index) => console.log(number * index));

const numbers = [10, 11, 12, 15, 20];

// Using the for each method, display only the even numbers in the array

numbers.forEach((number) => (number % 2 === 0 ? console.log(number) : false));

// SOME
// const numbers = [10, 11, 12, 15, 20];
// const isEven = numbers.some((number) => number % 2 === 0);
// console.log(isEven);

// Exercise
// const words = ['wow', 'hey', 'bye'];

// // Check if at least one element of the array starts with the letter 'h'

// const startsH = words.some((word) => word.startsWith('h'));
// console.log(startsH);

// EVERY

// const words = ['wow', 'hey', 'bye'];

// // Check if at least one element of the array starts with the letter 'h'

// const startsH = words.every((word) => word.startsWith('h'));
// console.log(startsH);

// Exercise
// const words = ['hello', 'hey', 'hola'];

// // Check if all the elements of the array start with the letter 'h'
// const beginH = words.every((word) => word.startsWith('h'));
// console.log(beginH);

// FILTER

// const numbers = [23, 345, 78, 4509, 9345, 999, 666, 234];

// let odds = numbers.filter((number) => number % 2 === 1);
// console.log(odds);

// REDUCE

// const arr = [9, 10, 11, 14];
// const total = arr.reduce((num, val) => {
//   console.log('num', num);
//   console.log('val', val);
//   console.log('val+num', val + num);
//   return num + val;
// });
// console.log(total);

// Exercise
// Use the reduce() method to sum up all the calories of every desert, except Apple Pie.

// The output should be 85

// let party = [
//   {
//     desert: 'Chocolate Mousse',
//     calories: 30
//   },
//   {
//     desert: 'Apple Pie',
//     calories: 15
//   },
//   {
//     desert: 'Croissant',
//     calories: 50
//   },
//   {
//     desert: 'Strawberry Icecream',
//     calories: 5
//   }
// ];

// let cals = party.reduce((num, obj) => {
//   return obj.desert !== 'Apple Pie' ? num + obj.calories : num + 0;
// }, 0);

// console.log(cals);

// DESTRUCTURING!!!!

// let arr = [44,99]
// let a = arr[0]
// let b = arr[1]

// let [a, b, ...rest] = [44, 99, 11, 213, 14324, 534];
// console.log(a);
// console.log(b);
// console.log(rest);

// let a = 'aardvark';
// let b = 'beaver';
// let bunch = ['cat', 'dog', 'elephant', 'flamingo', 'giraffe'];

// const aminals = [a, b, ...bunch];
// // console.log(aminals);

// const animals = [...aminals];

// animals[3] = 'dingo';

// console.log(aminals);
// console.log(animals);
