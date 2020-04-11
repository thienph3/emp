from flask import render_template, flash, redirect, request
from app.models.employee import Employee
from app.models.employee_form import EmployeeForm

def index():
    form = EmployeeForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            flash('Nhân viên {}, số CMND: {} khởi tạo thành công.'.format(form.name.data, form.cmnd.data))
            return redirect('/')
        #flash('Có gì đó sai sai.')
        #return render_template('employee/index.html', form=form)
    return render_template('employee/index.html', form=form)

def list():
    return render_template('employee/list.html', form=None)