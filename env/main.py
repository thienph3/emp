from flask import Flask, request
from app.controllers import employee_controller
import os

TEMPLATE_DIR = os.path.abspath('env/app/views')
STATIC_DIR = os.path.abspath('env/app/plugins')

print(TEMPLATE_DIR, STATIC_DIR)

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
print(app.template_folder, app.static_folder)

app.debug = True
app.config['SECRET_KEY'] = 'emp_secret'

@app.route('/', methods=['GET', 'POST'])
def index():
    return employee_controller.index()

@app.route('/list', methods=['GET', 'POST'])
def list():
    return employee_controller.list()


if __name__ == "__main__":
    app.run()