function insertRow() {
  const table = document.getElementById('sampleTable');

  const newRow = table.insertRow(-1);

  const cell1 = newRow.insertCell(0);
  const cell2 = newRow.insertCell(1);

  const size = table.rows.length + 1; // originally 3

  cell1.textContent = `Row${size} cell1`;
  cell2.textContent = `Row${size} cell2`;
}
