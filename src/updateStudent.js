/**
 * File: updateStudent.js
 * Initial Version: v1.1 (added in Release v1.1)
 * Implements: CR-02 - Update student details (name, department, year)
 *             with basic validation.
 *
 * Depends on:
 *  - searchStudent.js providing:
 *      window.findStudentById(id)
 *      window.getAllStudents()
 *      window.setStudents(updatedList)
 */

function loadStudentIntoForm() {
  const idInput = document.getElementById('editId');
  const nameInput = document.getElementById('editName');
  const deptInput = document.getElementById('editDepartment');
  const yearInput = document.getElementById('editYear');
  const messageEl = document.getElementById('editMessage');

  if (!idInput || !nameInput || !deptInput || !yearInput || !messageEl) return;

  const id = idInput.value.trim();
  messageEl.textContent = '';
  messageEl.className = 'message';

  if (!id) {
    messageEl.textContent = 'Please enter a Student ID to load.';
    messageEl.classList.add('error-text');
    return;
  }

  const existing = window.findStudentById ? window.findStudentById(id) : undefined;
  if (!existing) {
    messageEl.textContent = `No student found with ID: ${id}`;
    messageEl.classList.add('error-text');
    return;
  }

  nameInput.value = existing.name;
  deptInput.value = existing.department;
  yearInput.value = existing.year;

  messageEl.textContent = `Loaded student ${existing.id} for editing.`;
}

/**
 * Simple validation for student fields.
 */
function validateStudentFields(id, name, department, yearStr) {
  const errors = [];

  if (!id) {
    errors.push('Student ID is required.');
  }
  if (!name) {
    errors.push('Name is required.');
  }
  if (!department) {
    errors.push('Department is required.');
  }

  if (!yearStr) {
    errors.push('Year is required.');
  } else {
    const year = Number(yearStr);
    if (Number.isNaN(year) || year < 1 || year > 5) {
      errors.push('Year must be a number between 1 and 5.');
    }
  }

  return errors;
}

/**
 * Handle the edit form submit: validate and update in-memory data.
 * (No persistent file write is performed; this is sufficient for SCM demo.)
 */
function handleEditSubmit(event) {
  event.preventDefault();

  const idInput = document.getElementById('editId');
  const nameInput = document.getElementById('editName');
  const deptInput = document.getElementById('editDepartment');
  const yearInput = document.getElementById('editYear');
  const messageEl = document.getElementById('editMessage');

  if (!idInput || !nameInput || !deptInput || !yearInput || !messageEl) return;

  const id = idInput.value.trim();
  const name = nameInput.value.trim();
  const department = deptInput.value.trim();
  const yearStr = yearInput.value.trim();

  const errors = validateStudentFields(id, name, department, yearStr);
  messageEl.textContent = '';
  messageEl.className = 'message';

  if (errors.length > 0) {
    messageEl.textContent = errors.join(' ');
    messageEl.classList.add('error-text');
    return;
  }

  // Get existing list from searchStudent.js
  const allStudents = window.getAllStudents ? window.getAllStudents() : [];
  const index = allStudents.findIndex(
    (s) => s.id.toLowerCase() === id.toLowerCase()
  );

  if (index === -1) {
    messageEl.textContent = `Cannot update: no student found with ID: ${id}`;
    messageEl.classList.add('error-text');
    return;
  }

  const updatedYear = Number(yearStr);
  allStudents[index] = {
    ...allStudents[index],
    name,
    department,
    year: updatedYear,
  };

  // Push updated list back and refresh table
  if (window.setStudents) {
    window.setStudents(allStudents);
  }

  messageEl.textContent = `Student ${id} updated successfully. (In-memory only)`;
  messageEl.classList.add('success-text');
}

document.addEventListener('DOMContentLoaded', () => {
  const loadBtn = document.getElementById('loadStudentBtn');
  const editForm = document.getElementById('editForm');

  if (loadBtn) {
    loadBtn.addEventListener('click', loadStudentIntoForm);
  }
  if (editForm) {
    editForm.addEventListener('submit', handleEditSubmit);
  }
});


