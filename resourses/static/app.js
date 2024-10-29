const searchInput = document.getElementById('searchInput');
const tableRows = document.querySelectorAll('#disasterTable tbody tr'); // Updated to 'disasterTable'

const rowsPerPage = 10; // Adjust this value to change the number of rows per page
let currentPage = 1;

searchInput.addEventListener('input', (e) => {
  const searchTerm = e.target.value.toLowerCase();
  tableRows.forEach((row) => {
    const rowText = row.textContent.toLowerCase();
    if (rowText.includes(searchTerm)) {
      row.style.display = ''; // Show row if it matches
    } else {
      row.style.display = 'none'; // Hide row if it does not match
    }
  });
});
