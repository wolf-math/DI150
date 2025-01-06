let names = ['john', 'sarah', 23, 'Rudolf', 34];

// 1. Write a JavaScript for loop that will go through the variable names.

// if the item is not a string, pass.
// if the item is a string, check if its first letter is in uppercase. If not, change it to uppercase and then display the name.

for (item of names) {
  if (typeof item == 'string') {
    const name = item.charAt(0).toUpperCase() + item.slice(1);
    console.log(name);
  }
}

// 2. Write a JavaScript for loop that will go through the variable names

// if the item is not a string, go out of the loop.
// if the item is a string, display it.

for (item of names) {
  if (typeof item == 'string') {
    console.log(item);
  } else {
    break;
  }
}
