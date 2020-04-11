import json
from datetime import datetime
import os
from app.models.enum import Status

# CURRENT_WD = os.path.dirname(os.path.realpath(__file__))
CURRENT_WD = os.path.abspath('env/app')
LOCAL_FILE = CURRENT_WD + '/datas/database.json'

class Employee:
    def __init__(self, Name, CMND, Phone, Company, Reason, DueDate, Image=None, ID=0 , CreatedAt=None, Status=None, UpdatedAt=None):
        # import pdb
        # pdb.set_trace()
        self.ID = ID 
        self.Name = Name
        self.CMND = CMND
        self.Phone = Phone
        self.Company = Company
        self.Reason = Reason
        self.DueDate = DueDate
        self.Image = Image
        self.Status = Status
        self.CreatedAt = None
        self.UpdatedAt = None

    @staticmethod
    def createNewID():
        # import pdb
        # pdb.set_trace()
        with open(CURRENT_WD + '/datas/index.txt', 'r' ) as f:
            current_index = f.read()
            if current_index =='':
                id = 0
            else:
                id = int(current_index) + 1

        with open(CURRENT_WD + '/datas/index.txt', 'w+' ) as f:
            f.write(str(id))
        return id 

    @staticmethod
    def insertEmployeeToDatabase(employee):
        with open(LOCAL_FILE, 'a+') as f:
            f.write(employee) 
            f.write('\n')
        return True

    @staticmethod
    def insertEmployee(employee):
        # import pdb
        # pdb.set_trace()
        if employee.ID != 0:
            return False
        employee.ID = Employee.createNewID()
        employee.Status = Status.INIT.value
        employee.DueDate = employee.DueDate.strftime("%Y-%m-%d %H:%M:%S")
        employee.CreatedAt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        employee.UpdatedAt = employee.CreatedAt
        data = json.dumps(employee.__dict__)
        
        return insertEmployeeToDatabase(data)

    # thêm CreatedAt 
    @staticmethod
    def getEmployeesByStatus(status):
        data = []
        with open(LOCAL_FILE, 'r') as f:
            data = f.readlines()
            result  = [] 
            for row in data: 
                row = json.loads(row)
                if row.get(Status) in status or len(status) == 0:
                    result.append(row)
        return result

# thêm updated at 
    @staticmethod
    def getEmployeeByID(id):
        # import pdb
        # pdb.set_trace()
        with open(LOCAL_FILE, 'r') as f:
            for line in f:
                row = json.loads(line)
                if row.get('ID') == id:
                    result = Employee(**row)
        return result

    @staticmethod
    def updateEmployeeByID(employee):
        emp = Employee.getEmployeeByID(employee.ID)
        if emp is None:
            return False
        if !((emp.Status == 0 and employee.Status in (1, 2)) or (emp.Status == 2 and employee.Staus == 1)):
            return False
        emp.Status = employee.Status
        emp.UpdatedAt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        return insertEmployeeToDatabase(emp)
    
if __name__ == "__main__":
    _new_emp = {'Name' : 'MaiAnh_123', 
                'CMND': 123456, 
                'Phone': 78910, 
                'Company': 'ABC' , 
                'Reason': 'new', 
                'DueDate': '2020-03-04', 
                'Image': None }
    __test_dict = { 'ID' : 7,
                    'Name' : 'MaiAnh_123', 
                    'CMND': 123456, 
                    'Phone': 78910, 
                    'Company': 'ABC' , 
                    'Reason': 'new', 
                    'DueDate': '2020-03-04', 
                    'Image': None }
    # print(type(__test_dict))
    Employee.insertEmployee(Employee(**_new_emp))
    maianh_07 = Employee(**__test_dict)
    # print(maianh_07)
    # print(maianh_07.ID)
    # print(maianh)
    # Employee.getEmployeeByID(7)
    # Employee.updateEmployeeByID(maianh_07)
    # Employee.getEmployeesByStatus(0)