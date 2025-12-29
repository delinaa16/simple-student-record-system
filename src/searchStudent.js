/**
 * File: searchStudent.js
 * Initial Version: v1.1 (added in Release v1.1)
 * Implements: CR-01 - Search functionality for student records by student ID.
 *
 * Responsibility:
 *  - Load students from database.json
 *  - Render the main student table
 *  - Filter/search by Student ID
 *  - Expose helper functions for other modules (e.g., updateStudent.js)
 */

let students = [];

/**
 * Load students from the local JSON "database".
 * Note: For browsers, this should be served via HTTP (e.g., simple local server)
 * so that fetch('database.json') is allowed.
 */
async function loadStudents() {
  try {
    const response = await fetch('database.json');
    if (!response.ok) {
      throw new Error('Failed to load database.json');
    }
    const data = await response.json();
    // Expecting an array of student objects
    students = Array.isArray(data) ? data : [];
    renderStudents(students);
  } catch (error) {
    console.error(error);
    const messageEl = document.getElementById('searchMessage');
    if (messageEl) {
      messageEl.textContent =
        'Unable to load student data. Please check database.json.';
      messageEl.classList.add('error-text');
    }
  }
}

/**
 * Render the student table body with the given list.
 */
function renderStudents(list) {
  const tbody = document.getElementById('studentTableBody');
  if (!tbody) return;

  tbody.innerHTML = '';

  list.forEach((student) => {
    const tr = document.createElement('tr');

    const tdId = document.createElement('td');
    tdId.textContent = student.id;

    const tdName = document.createElement('td');
    tdName.textContent = student.name;

    const tdDept = document.createElement('td');
    tdDept.textContent = student.department;

    const tdYear = document.createElement('td');
    tdYear.textContent = student.year;

    tr.appendChild(tdId);
    tr.appendChild(tdName);
    tr.appendChild(tdDept);
    tr.appendChild(tdYear);

    // Optional: when clicking a row, copy ID into edit form
    tr.addEventListener('click', () => {
      const editIdInput = document.getElementById('editId');
      if (editIdInput) {
        editIdInput.value = student.id;
      }
    });

    tbody.appendChild(tr);
  });
}

/**
 * Find a single student by ID in the loaded list.
 */
function findStudentById(id) {
  if (!id) return undefined;
  return students.find((s) => s.id.toLowerCase() === id.toLowerCase());
}

/**
 * Handle the search form submit (CR-01).
 */
function handleSearch(event) {
  event.preventDefault();
  const idInput = document.getElementById('searchId');
  const messageEl = document.getElementById('searchMessage');
  if (!idInput || !messageEl) return;

  const query = idInput.value.trim();
  messageEl.textContent = '';
  messageEl.className = 'message';

  if (!query) {
    // Empty search -> show all
    renderStudents(students);
    return;
  }

  const match = findStudentById(query);
  if (!match) {
    renderStudents([]);
    messageEl.textContent = `No student found with ID: ${query}`;
    messageEl.classList.add('error-text');
  } else {
    renderStudents([match]);
    messageEl.textContent = `Showing result for ID: ${match.id}`;
  }
}

/**
 * Reset the search and show all students.
 */
function resetSearch() {
  const idInput = document.getElementById('searchId');
  const messageEl = document.getElementById('searchMessage');
  if (idInput) idInput.value = '';
  if (messageEl) {
    messageEl.textContent = '';
    messageEl.className = 'message';
  }
  renderStudents(students);
}

/**
 * Expose minimal shared API for updateStudent.js:
 *  - window.findStudentById
 *  - window.getAllStudents
 *  - window.setStudents
 */
window.findStudentById = findStudentById;
window.getAllStudents = function () {
  return students.slice();
};
window.setStudents = function (updatedList) {
  students = Array.isArray(updatedList) ? updatedList : [];
  renderStudents(students);
};

document.addEventListener('DOMContentLoaded', () => {
  // Initial data load
  loadStudents();

  // Wire up search form events
  const searchForm = document.getElementById('searchForm');
  const resetBtn = document.getElementById('resetSearch');
  if (searchForm) {
    searchForm.addEventListener('submit', handleSearch);
  }
  if (resetBtn) {
    resetBtn.addEventListener('click', resetSearch);
  }
});


