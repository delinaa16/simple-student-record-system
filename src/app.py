"""
File: app.py
Version: v1.0
Description: Flask web server for Student Record Management System
Purpose: Provides web API endpoints for the frontend HTML/JS application

For SCM Mini Project - Simple Student Record Management System
"""

from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import os
import sys

# Import functions from student_record.py
sys.path.insert(0, os.path.dirname(__file__))
from student_record import (
    load_database,
    save_database,
    find_student_by_id,
    get_all_students,
    add_student,
    update_student,
    delete_student,
    search_students
)

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)  # Enable CORS for cross-origin requests

# Change working directory to src folder
os.chdir(os.path.dirname(os.path.abspath(__file__)))


@app.route('/')
def index():
    """Serve the login page"""
    return send_from_directory('.', 'login_page.html')


@app.route('/dashboard.html')
def dashboard():
    """Serve the dashboard page"""
    return send_from_directory('.', 'dashboard.html')


@app.route('/style.css')
def style():
    """Serve the CSS file"""
    return send_from_directory('.', 'style.css')


@app.route('/database.json')
def get_database():
    """API endpoint: Get all students"""
    try:
        students = get_all_students()
        return jsonify(students), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/students', methods=['GET'])
def api_get_students():
    """API endpoint: Get all students"""
    try:
        students = get_all_students()
        return jsonify(students), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/students/<student_id>', methods=['GET'])
def api_get_student(student_id):
    """API endpoint: Get student by ID"""
    try:
        student = find_student_by_id(student_id)
        if student:
            return jsonify(student), 200
        else:
            return jsonify({'error': 'Student not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/students/search', methods=['GET'])
def api_search_students():
    """API endpoint: Search students"""
    try:
        query = request.args.get('q', '')
        if not query:
            students = get_all_students()
        else:
            students = search_students(query)
        return jsonify(students), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/students', methods=['POST'])
def api_add_student():
    """API endpoint: Add a new student"""
    try:
        data = request.get_json()
        student_id = data.get('id')
        name = data.get('name')
        department = data.get('department')
        year = data.get('year')
        
        if not all([student_id, name, department, year]):
            return jsonify({'error': 'Missing required fields'}), 400
        
        if add_student(student_id, name, department, year):
            return jsonify({'message': 'Student added successfully'}), 201
        else:
            return jsonify({'error': 'Failed to add student'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/students/<student_id>', methods=['PUT'])
def api_update_student(student_id):
    """API endpoint: Update a student"""
    try:
        data = request.get_json()
        name = data.get('name')
        department = data.get('department')
        year = data.get('year')
        
        if update_student(student_id, name, department, year):
            return jsonify({'message': 'Student updated successfully'}), 200
        else:
            return jsonify({'error': 'Failed to update student'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/students/<student_id>', methods=['DELETE'])
def api_delete_student(student_id):
    """API endpoint: Delete a student"""
    try:
        if delete_student(student_id):
            return jsonify({'message': 'Student deleted successfully'}), 200
        else:
            return jsonify({'error': 'Student not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    print("=" * 50)
    print("Student Record Management System - Web Server")
    print("=" * 50)
    print("\nStarting Flask server...")
    print("Open your browser and go to: http://localhost:5000")
    print("Press Ctrl+C to stop the server\n")
    app.run(debug=True, host='0.0.0.0', port=5000)

