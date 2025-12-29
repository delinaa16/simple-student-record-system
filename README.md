# Simple Student Record Management System (SSRMS)

---

## Project Overview

This is a **simple student record management system** implemented for the **Software Configuration Management (SCM) mini-project**.  
The focus is on **SCM processes**, including version control, baselines, change requests, and releases.

---

## Release Notes

### Release v1.0

- **Product:** Simple Student Record Management System  
- **Version:** v1.0  
- **Release Date:** 2025-12-30  
- **Baseline Reference:** BL1 – Initial Repository Setup  

#### Overview
Initial working prototype focused on establishing repository structure, configuration items, and minimal UI.

#### Features
- Repository structure: `/docs`, `/src`, `/tests`, `/releases`  
- Login page (`src/login_page.html`) – simple front-end only  
- Dashboard (`src/dashboard.html`) – basic student list layout  
- Sample data (`src/database.json`) – initial student records  
- Styling (`src/style.css`) – basic layout and typography  

#### Known Limitations
- No persistent backend or authentication  
- Minimal UI functionality  
- Search and update features not implemented  

---

### Release v1.1

- **Product:** Simple Student Record Management System  
- **Version:** v1.1  
- **Release Date:** 2025-12-30  
- **Baseline Reference:** BL2 – Prototype + CR Implementations  

#### Overview
Enhanced version implementing three formal Change Requests (CRs):  
- **CR-01:** Search student by ID  
- **CR-02:** Update student details with validation  
- **CR-03:** Improve form alignment and readability  

#### Features / Changes
- Dashboard updated with search panel and edit form  
- JavaScript modules: `searchStudent.js`, `updateStudent.js`  
- Styling improvements for forms and tables  
- All updates applied in-memory (client-side)  

#### Known Limitations
- Client-side authentication only  
- Updates do not persist to server  
- No automated tests yet  

---

## Team Members and Responsibilities

| Name               | ID          | Key Contributions |
|-------------------|------------|-----------------|
| Birhan Aklilu      | ETS0363/14 | Maintain Change Log, baseline documentation |
| Burka Labsi        | ETS0402/14 | Package releases, document release notes |
| Dagm Taye          | ETS0412/14 | Implement core student logic, front-end pages |
| Dagmawit Gebreweld | ETS0435/14 | Maintain CI Register, requirements document |
| Dagmawit Negash    | ETS0436/14 | Prepare developer guide, Change Request template |
| Danayt Esayas      | ETS0438/14 | Prepare SCMP and user manual |
| Delina Mulubirhan  | ETS0484/14 | **Pushed all project files, prepared test cases and results** |

---

## Approval

- **SCM Manager:** Dagmawit Gebreweld  
- **v1.0 Decision:** Initial prototype approved (BL1)  
- **v1.1 Decision:** Updated prototype approved with CR-01, CR-02, CR-03 (BL2)  
- **Approval Date:** 2025-12-29
