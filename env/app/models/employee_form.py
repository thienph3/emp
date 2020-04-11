from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField
from wtforms.validators import DataRequired, Length

class EmployeeForm(FlaskForm):
    Name = StringField('Họ tên', validators=[DataRequired(message=('Chưa nhập họ tên'))])
    CMND = StringField('CMND', validators=[DataRequired(message=('Chưa nhập CMND'))])
    Phone = StringField('Số điện thoại')
    Company = StringField('Nhà thầu')
    Reason = StringField('Lí do')
    DueDate = DateField('Ngày hết hạn', validators=[DataRequired(message=('Chưa nhập ngày hết hạn'))], format='%d/%m/%Y')
    Image = StringField('Ảnh chân dung')
    Submit = SubmitField('Thêm nhân viên mới')