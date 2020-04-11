from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField
from wtforms.validators import DataRequired, Length

class EmployeeForm(FlaskForm):
    name = StringField('Họ tên', validators=[DataRequired(message=('Chưa nhập họ tên'))])
    cmnd = StringField('CMND', validators=[DataRequired(message=('Chưa nhập CMND'))])
    phone = StringField('Số điện thoại')
    company = StringField('Nhà thầu')
    reason = StringField('Lí do')
    dueDate = DateField('Ngày hết hạn', validators=[DataRequired(message=('Chưa nhập ngày hết hạn'))], format='%d/%m/%Y')
    image = StringField('Ảnh chân dung')
    submit = SubmitField('Thêm nhân viên mới')