from flask import render_template
from app.models.employee import Employee

def index():
    e = Employee('Name vớ vẩn (cái name này là do controller truyền vào nhá)')
    return render_template('employee/index.html', data=e)