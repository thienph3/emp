from flask import Flask
from app.controllers import employee_controller
app = Flask(__name__, template_folder='app/views')
#print(app.template_folder)
app.debug = True

@app.route('/')
def index():
    return employee_controller.index()

if __name__ == "__main__":
    app.run()