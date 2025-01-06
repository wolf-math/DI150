// For each of the questions, find 2 WAYS of accessing :

// 1. The div DOM node?

// 2. The ul DOM node?

// 3. The second li (with Pete)?

const div1 = document.body.firstElementChild;
const div2 = document.body.children[0];

console.log(div1);
console.log(div2);

const ul1 = document.body.children[1];
const ul2 = div1.nextElementSibling;

console.log(ul1);
console.log(ul2);

const pete = ul1.lastElementChild;
const pete2 = ul1.children[1];

console.log(pete);
console.log(pete2);
