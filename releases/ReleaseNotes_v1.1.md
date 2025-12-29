# Release Notes – Version 1.1

**Product:** Simple Student Record Management System  
**Release Version:** v1.1  
**Release Date:** 2025-12-30  
**Baseline Reference:** BL2 – Prototype + CR Implementations  
**SCM Manager (Approved by):** Dagmawit Gebreweld  

---

## 1. Overview

Release v1.1 is an enhanced version of the Simple Student Record Management System that builds on the initial  
prototype (Release v1.0) and implements three formal Change Requests:

- **CR-01:** Search for student records by Student ID  
- **CR-02:** Update student details (name, department, year) with validation  
- **CR-03:** Improve form alignment, spacing, and readability  

This release is associated with **Baseline BL2**, which includes BL1 plus all implemented source code and updated documents.

---

## 2. Baseline Reference

- **Baseline ID:** BL2  
- **Baseline Name:** Prototype with Change Requests Implemented  
- **Included Artifacts:**  
  - All items from BL1 (SCMP, CI Register, Requirements, User Manual, Developer Guide, and initial repo structure)  
  - Source code for login, dashboard, styling, search, and update logic  
  - `database.json` with initial student records  
  - Baseline records (`BaselineRecord_BL1.md`, `BaselineRecord_BL2.md`)  
  - Release notes (`ReleaseNotes_v1.0.md`, `ReleaseNotes_v1.1.md`)  

Release v1.1 is built directly on BL2, which is the authoritative configuration for this version.

---

## 3. Features / Changes in v1.1

### 3.1 Core Functional Features

1. **Login Page (unchanged behavior, documented)**
   - **File:** `src/login_page.html` (v0.1)  
   - **Status:** Included in v1.0 and v1.1 (no CR changes).  
   - **Behavior:**  
     - Accepts any non-empty username and password and navigates to `dashboard.html`.  
   - **Comments:** File header documents version and release usage.  

2. **Student Dashboard (updated to v1.1)**
   - **File:** `src/dashboard.html` (v1.1)  
   - **Changes from v0.1 to v1.1:**  
     - Integrated a **Search panel** for student ID search (CR-01).  
     - Integrated an **Edit Student Record** form for updating student details (CR-02).  
     - Connected to the JavaScript modules `searchStudent.js` and `updateStudent.js`.  
   - **Result:**  
     - Users can view the list of students, search by ID, and open/edit student records in the form.  

3. **Search Functionality (CR-01)**
   - **File:** `src/searchStudent.js` (v1.1)  
   - **Key Responsibilities:**  
     - Load student data from `database.json`.  
     - Render the student list into the table on `dashboard.html`.  
     - Filter students by ID when the user submits the search form.  
     - Expose helper functions (`findStudentById`, `getAllStudents`, `setStudents`) for use by other scripts.  
   - **User Impact:**  
     - A student can be quickly located by entering their ID (e.g., `S001`) and clicking **Search**.  

4. **Update Functionality (CR-02)**
   - **File:** `src/updateStudent.js` (v1.1)  
   - **Key Responsibilities:**  
     - Load a selected student into the edit form based on Student ID.  
     - Validate that ID, name, department, and year are provided and that year is between 1 and 5.  
     - Update the in-memory student record and refresh the table view.  
   - **User Impact:**  
     - A user can modify the name, department, or year of an existing student and see the updated data immediately in the table.  
   - **Note:**  
     - Changes are applied in-memory on the client side (sufficient for SCM mini-project demonstration).  

5. **Styling and Layout Improvements (CR-03)**
   - **File:** `src/style.css` (v1.1)  
   - **Key Improvements:**  
     - Better alignment of labels and inputs (especially on small screens).  
     - Use of grid layout for the edit form for clarity and readability.  
     - Enhanced button styling, spacing, messages, and table aesthetics.  
   - **User Impact:**  
     - Cleaner UI for both login and dashboard pages, improving usability and readability.  

6. **Student Data Store**
   - **File:** `src/database.json` (v0.1)  
   - **Description:**  
     - Contains sample students with `id`, `name`, `department`, and `year`.  
     - Used by `searchStudent.js` to populate the dashboard table.  
   - **Changes in v1.1:**  
     - No structural changes; reused as-is from v1.0, still suitable for CR-01 and CR-02.  

---

## 4. Change Request (CR) Implementations in v1.1

### 4.1 CR-01 – Search by Student ID

- **Objective:** Allow users to search for a specific student by entering their Student ID.  
- **Implemented In:**  
  - `dashboard.html` – Search form UI and message area.  
  - `searchStudent.js` – Logic for data loading, rendering, and filtering by ID.  
- **Result:**  
  - Users can search for a student using their ID and see either a single matching row or a "no student found" message.  

### 4.2 CR-02 – Update Student Details with Validation

- **Objective:** Enable editing of student name, department, and year with basic validation.  
- **Implemented In:**  
  - `dashboard.html` – Edit form UI and action buttons (`Load Student by ID`, `Save Changes`).  
  - `updateStudent.js` – Input validation, record update, and table refresh logic.  
- **Validation Rules:**  
  - Student ID, Name, and Department are required.  
  - Year must be a number between 1 and 5.  
- **Result:**  
  - Users can safely update student details while being notified of invalid input.  

### 4.3 CR-03 – Improve Form Alignment and Readability

- **Objective:** Improve the user experience with better form alignment, spacing, and responsive layout.  
- **Implemented In:**  
  - `style.css` – Updated classes like `.form-group`, `.form-grid`, `.form-card`, `.form-actions`, and button styles.  
- **Result:**  
  - The dashboard and login interfaces look cleaner, have consistent spacing, and adapt better to smaller screens.  

---

## 5. Known Limitations in v1.1

- Authentication is still client-side only and not backed by a real server.  
- Updates to student records are in-memory only and do not persist to disk on the server.  
- No automated tests are included yet in `/tests`.  

These limitations are acceptable for the scope of the SCM mini-project and can be addressed in future CRs if needed.

---

## 6. Approval

- **SCM Manager:** Dagmawit Gebreweld  
- **Decision:** Release v1.1 is approved as the updated prototype release based on Baseline BL2, including CR-01, CR-02, and CR-03.  
- **Approval Date:** 2025-12-30  

This release will be used for configuration audits (PCA/FCA) and final project submission.


