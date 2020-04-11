from flask import Flask, request
from app.controllers import employee_controller
import os, json

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

@app.route('/list', methods=['GET'])
def list():
    return employee_controller.list()

@app.route('/update', methods=['POST'])
def update():
    d = {}
    for i in [i.split('=') for i in request.data.decode('utf-8').split('&')]:
        d[i[0]] = int(i[1])
    ID = d['ID']
    Status = d['Status']
    return str(employee_controller.update(ID, Status))


if __name__ == "__main__":
    app.run()