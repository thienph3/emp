from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField
from wtforms.validators import DataRequired

class EmployeeForm(FlaskForm):
    name = StringField('Họ tên', validators=[DataRequired()])
    cmnd = StringField('CMND', validators=[DataRequired()])
    phone = StringField('Số điện thoại')
    company = StringField('Nhà thầu')
    reason = StringField('Lí do')
    dueDate = DateField('Ngày hết hạn', validators=[DataRequired()], format='%d/%m/%Y')
    image = StringField('Ảnh chân dung')
    submit = SubmitField('Thêm nhân viên mới')