const winCombos = [
  [0, 1, 2],
  [3, 4, 5],
  [6, 7, 8],
  [0, 3, 6],
  [1, 4, 7],
  [2, 5, 8],
  [0, 4, 8],
  [6, 4, 2]
];

const board = document.getElementById('board');

for (let i = 0; i < 10; i++) {
  const div = document.createElement('div');
  div.id = i;
}
