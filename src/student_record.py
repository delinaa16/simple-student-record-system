"""
File: student_record.py
Version: v1.0
Description: Python backend script for Student Record Management System
Purpose: Provides server-side functionality for managing student records
         Can be used as a simple backend API or CLI tool

For SCM Mini Project - Simple Student Record Management System
"""

import json
import os
from typing import List, Dict, Optional

# Database file path
DATABASE_FILE = 'database.json'


def load_database() -> List[Dict]:
    """
    Load student records from JSON database file.
    
    Returns:
        List of student dictionaries
    """
    if not os.path.exists(DATABASE_FILE):
        # Create empty database if it doesn't exist
        save_database([])
        return []
    
    try:
        with open(DATABASE_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error loading database: {e}")
        return []


def save_database(students: List[Dict]) -> bool:
    """
    Save student records to JSON database file.
    
    Args:
        students: List of student dictionaries
        
    Returns:
        True if successful, False otherwise
    """
    try:
        with open(DATABASE_FILE, 'w', encoding='utf-8') as f:
            json.dump(students, f, indent=2, ensure_ascii=False)
        return True
    except IOError as e:
        print(f"Error saving database: {e}")
        return False


def find_student_by_id(student_id: str) -> Optional[Dict]:
    """
    Find a student by their ID (case-insensitive).
    
    Args:
        student_id: Student ID to search for
        
    Returns:
        Student dictionary if found, None otherwise
    """
    students = load_database()
    for student in students:
        if student.get('id', '').lower() == student_id.lower():
            return student
    return None


def get_all_students() -> List[Dict]:
    """
    Get all student records.
    
    Returns:
        List of all student dictionaries
    """
    return load_database()


def add_student(student_id: str, name: str, department: str, year: int) -> bool:
    """
    Add a new student record.
    
    Args:
        student_id: Unique student ID
        name: Student name
        department: Department name
        year: Academic year (1-5)
        
    Returns:
        True if added successfully, False if ID already exists
    """
    students = load_database()
    
    # Check if student ID already exists
    if find_student_by_id(student_id):
        print(f"Error: Student with ID {student_id} already exists.")
        return False
    
    # Validate year
    if not (1 <= year <= 5):
        print(f"Error: Year must be between 1 and 5.")
        return False
    
    new_student = {
        'id': student_id,
        'name': name,
        'department': department,
        'year': year
    }
    
    students.append(new_student)
    return save_database(students)


def update_student(student_id: str, name: str = None, department: str = None, year: int = None) -> bool:
    """
    Update an existing student record.
    
    Args:
        student_id: Student ID to update
        name: New name (optional)
        department: New department (optional)
        year: New year (optional, must be 1-5)
        
    Returns:
        True if updated successfully, False otherwise
    """
    students = load_database()
    
    # Find student index
    index = None
    for i, student in enumerate(students):
        if student.get('id', '').lower() == student_id.lower():
            index = i
            break
    
    if index is None:
        print(f"Error: Student with ID {student_id} not found.")
        return False
    
    # Validate year if provided
    if year is not None and not (1 <= year <= 5):
        print(f"Error: Year must be between 1 and 5.")
        return False
    
    # Update fields
    if name:
        students[index]['name'] = name
    if department:
        students[index]['department'] = department
    if year is not None:
        students[index]['year'] = year
    
    return save_database(students)


def delete_student(student_id: str) -> bool:
    """
    Delete a student record by ID.
    
    Args:
        student_id: Student ID to delete
        
    Returns:
        True if deleted successfully, False otherwise
    """
    students = load_database()
    
    # Find and remove student
    original_count = len(students)
    students = [s for s in students if s.get('id', '').lower() != student_id.lower()]
    
    if len(students) == original_count:
        print(f"Error: Student with ID {student_id} not found.")
        return False
    
    return save_database(students)


def search_students(query: str) -> List[Dict]:
    """
    Search students by ID, name, or department (case-insensitive).
    
    Args:
        query: Search query string
        
    Returns:
        List of matching student dictionaries
    """
    students = load_database()
    query_lower = query.lower()
    
    results = []
    for student in students:
        if (query_lower in student.get('id', '').lower() or
            query_lower in student.get('name', '').lower() or
            query_lower in student.get('department', '').lower()):
            results.append(student)
    
    return results


# CLI interface for testing
if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 2:
        print("Student Record Management System - Python CLI")
        print("\nUsage:")
        print("  python student_record.py list                    - List all students")
        print("  python student_record.py search <query>           - Search students")
        print("  python student_record.py find <id>                - Find student by ID")
        print("  python student_record.py add <id> <name> <dept> <year>  - Add student")
        print("  python student_record.py update <id> [name] [dept] [year]  - Update student")
        print("  python student_record.py delete <id>              - Delete student")
        sys.exit(1)
    
    command = sys.argv[1].lower()
    
    if command == 'list':
        students = get_all_students()
        if not students:
            print("No students found.")
        else:
            print(f"\nTotal students: {len(students)}\n")
            for student in students:
                print(f"ID: {student.get('id')}")
                print(f"  Name: {student.get('name')}")
                print(f"  Department: {student.get('department')}")
                print(f"  Year: {student.get('year')}\n")
    
    elif command == 'search':
        if len(sys.argv) < 3:
            print("Error: Please provide a search query.")
            sys.exit(1)
        query = sys.argv[2]
        results = search_students(query)
        if not results:
            print(f"No students found matching '{query}'.")
        else:
            print(f"\nFound {len(results)} student(s):\n")
            for student in results:
                print(f"ID: {student.get('id')}, Name: {student.get('name')}, "
                      f"Department: {student.get('department')}, Year: {student.get('year')}")
    
    elif command == 'find':
        if len(sys.argv) < 3:
            print("Error: Please provide a student ID.")
            sys.exit(1)
        student = find_student_by_id(sys.argv[2])
        if student:
            print(f"\nStudent found:")
            print(f"  ID: {student.get('id')}")
            print(f"  Name: {student.get('name')}")
            print(f"  Department: {student.get('department')}")
            print(f"  Year: {student.get('year')}")
        else:
            print(f"Student with ID '{sys.argv[2]}' not found.")
    
    elif command == 'add':
        if len(sys.argv) < 6:
            print("Error: Usage: python student_record.py add <id> <name> <dept> <year>")
            sys.exit(1)
        student_id = sys.argv[2]
        name = sys.argv[3]
        department = sys.argv[4]
        try:
            year = int(sys.argv[5])
            if add_student(student_id, name, department, year):
                print(f"Student {student_id} added successfully.")
            else:
                sys.exit(1)
        except ValueError:
            print("Error: Year must be a number.")
            sys.exit(1)
    
    elif command == 'update':
        if len(sys.argv) < 3:
            print("Error: Please provide a student ID.")
            sys.exit(1)
        student_id = sys.argv[2]
        name = sys.argv[3] if len(sys.argv) > 3 else None
        department = sys.argv[4] if len(sys.argv) > 4 else None
        year = int(sys.argv[5]) if len(sys.argv) > 5 else None
        
        if update_student(student_id, name, department, year):
            print(f"Student {student_id} updated successfully.")
        else:
            sys.exit(1)
    
    elif command == 'delete':
        if len(sys.argv) < 3:
            print("Error: Please provide a student ID.")
            sys.exit(1)
        if delete_student(sys.argv[2]):
            print(f"Student {sys.argv[2]} deleted successfully.")
        else:
            sys.exit(1)
    
    else:
        print(f"Error: Unknown command '{command}'.")
        sys.exit(1)

