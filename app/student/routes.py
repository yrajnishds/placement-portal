from flask import render_template
from app.student import student


@student.route('/dashboard')
def dashboard():
    return render_template('student/dashboard.html')