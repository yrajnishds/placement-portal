from flask import render_template
from app.company import company


@company.route('/dashboard')
def dashboard():
    return render_template('company/dashboard.html')