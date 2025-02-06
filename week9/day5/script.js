// Exercise
// Use the methods above to :

// Count how many keys and values are in the object below
// Display : "The x# key is : --- The x# value is : ---".

let myObj = {
  name: 'John',
  lastName: 'Doe',
  age: 25,
  friends: ['Mark', 'Lucie', 'Ana']
};

// const myArr = Object.entries(myObj);
// console.log(myArr);

// myArr.forEach((key, index) =>
//   console.log(
//     `The ${index} key is : ${key[0]} The ${index} value is : ${key[1]}`
//   )
// );

const myKeys = Object.keys(myObj);

myKeys.forEach((key, index) =>
  console.log(
    `The ${index} key is : ${key} The ${index} value is : ${myObj[key]}`
  )
);
