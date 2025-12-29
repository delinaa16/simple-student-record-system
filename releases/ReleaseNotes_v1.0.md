# Release Notes – Version 1.0

**Product:** Simple Student Record Management System  
**Release Version:** v1.0  
**Release Date:** 2025-12-30  
**Baseline Reference:** BL1 – Initial Repository Setup  
**SCM Manager (Approved by):** Dagmawit Gebreweld  

---

## 1. Overview

Release v1.0 represents the initial working prototype of the Simple Student Record Management System.  
This release is primarily focused on establishing the basic structure, configurations, and a minimal  
user-facing interface that can later be extended through change requests (CRs).

The emphasis of this release is on **SCM processes**, including:

- Initial baseline creation (BL1)  
- Initial repository structure and configuration item identification  
- Documentation of SCM Plan, CI Register, and supporting documents  

---

## 2. Baseline Reference

- **Baseline ID:** BL1  
- **Baseline Name:** Initial Repository Setup  
- **Included Artifacts:**  
  - `SCMP_v1.0.docx`  
  - `CI_Register.docs`  
  - `Requirements_v1.0.docx`  
  - `User_Manual_v1.0.docx`  
  - `Developer_Guide_v1.0.docx`  
  - Repository folders: `/docs`, `/src`, `/tests`, `/releases`  

Release v1.0 is built directly on BL1. No formal change requests (CRs) are implemented yet in this release.

---

## 3. Features Included in v1.0

### 3.1 Repository and Structure

- GitHub repository `Simple_StudentRecord_SCMP` created with standard structure:
  - `/docs` – SCM plan, CI register, requirements, user and developer documents  
  - `/src` – Placeholder for source files  
  - `/tests` – Placeholder for future tests  
  - `/releases` – Placeholder for packaged release artifacts  

### 3.2 Initial User Interface (Prototype)

1. **Login Page**
   - **File:** `src/login_page.html` (v0.1)  
   - **Description:**  
     - Simple login form with username and password fields and a submit button.  
     - Front-end only; any non-empty credentials allow navigation to the dashboard page (prototype behavior).  
   - **Notes:**  
     - Intended as a minimal UI prototype and entry point for the system.  

2. **Dashboard Page (v0.1 Prototype View)**
   - **File:** `src/dashboard.html` (initial v0.1 state)  
   - **Description:**  
     - Basic layout for a student dashboard page listing students and showing fields for ID, name, department, and year.  
     - At this stage, functionality is minimal and is meant as a placeholder for later CR implementations.  

3. **Sample Data**
   - **File:** `src/database.json` (v0.1)  
   - **Description:**  
     - Contains initial sample student records with fields: `id`, `name`, `department`, and `year`.  
     - Used as the simple data source for demonstrating the student record concept.  

4. **Styling**
   - **File:** `src/style.css` (v0.1)  
   - **Description:**  
     - Basic styling for login and dashboard layouts (typography, colors, simple layout).  
     - Forms and tables are functional but not yet refined.  

---

## 4. Change Requests (CR) in v1.0

- No formal Change Requests (CR-01, CR-02, CR-03) are implemented in Release v1.0.  
- CRs will be designed and applied in the subsequent baseline (BL2) and Release v1.1.  

---

## 5. Known Limitations in v1.0

- Search functionality is not yet implemented.  
- Update/edit functionality for student records is not yet implemented.  
- Form alignment and advanced styling improvements are not yet applied.  
- No persistent backend or real authentication (prototype only).  

These limitations are intentionally left for future releases and will be addressed through CR-01, CR-02, and CR-03 in v1.1.

---

## 6. Approval

- **SCM Manager:** Dagmawit Gebreweld  
- **Decision:** Release v1.0 is approved as the initial prototype release based on Baseline BL1.  
- **Approval Date:** 2025-12-30  

This release will serve as the reference point for tracking subsequent changes and enhancements in Release v1.1.


