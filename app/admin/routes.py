from flask import render_template
from app.admin import admin


@admin.route('/dashboard')
def dashboard():
    return render_template('admin/dashboard.html')