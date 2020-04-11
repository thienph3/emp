from flask import render_template, flash, redirect, request
from app.models.employee import Employee
from app.models.employee_form import EmployeeForm
from datetime import datetime

def getEmployee(form):
    return Employee(form.Name.data, form.CMND.data, form.Phone.data, form.Company.data, form.Reason.data, form.DueDate.data, form.Image.data, 0, datetime.now(), 0, datetime.now())

def index():
    form = EmployeeForm()
    if form.validate_on_submit():
        if Employee.insertEmployee(getEmployee(form)):
            flash('Nhân viên {}, số CMND: {} khởi tạo thành công.'.format(form.Name.data, form.CMND.data))
        else:
            flash('Có gì đó sai sai.')
        return redirect('/')
    return render_template('employee/index.html', form=form)

def list():
    list = Employee.getEmployeesByStatus([])
    print(list)
    #if form.validate_on_submit():
    #    if False:
    #        flash('Test')
    #    else:
    #        flash('Có gì đó sai sai.')
    #    return redirect('/list')
    return render_template('employee/list.html', list=list)