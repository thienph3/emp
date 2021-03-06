import json
from datetime import datetime
import os
from app.models.enum import Status

# CURRENT_WD = os.path.dirname(os.path.realpath(__file__))
CURRENT_WD = os.path.abspath('env/app')
LOCAL_FILE = CURRENT_WD + '/datas/database.json'

class Employee:
    def __init__(self, Name=None, CMND=None, Phone=None, Company=None, Reason=None, DueDate=None, Image=None, ID=0 , CreatedAt=None, Status=None, UpdatedAt=None):
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
        self.CreatedAt = CreatedAt
        self.UpdatedAt = UpdatedAt

    @staticmethod
    def datetime_to_string(cols, e, format_string):
        if e[cols] is not None:
            return datetime.strptime(e[cols], format_string) 
        else:
            return None

    @staticmethod
    def cast(e):
        # e = json.loads(e)
        e['DueDate'] = Employee.datetime_to_string('DueDate', e, "%Y-%m-%d") 
        e['CreatedAt'] = Employee.datetime_to_string('CreatedAt', e, "%Y-%m-%d %H:%M:%S") 
        e['UpdatedAt'] = Employee.datetime_to_string('UpdatedAt', e, "%Y-%m-%d %H:%M:%S") 
        return Employee(**e)
        # return Employee(e['Name'], e['CMND'], e['Phone'], e['Company'], e['Reason'], e['DueDate'], e['Image'], e['ID'], e['CreatedAt'], e['Status'], e['UpdatedAt'])

    @staticmethod
    def createNewID():
        with open(CURRENT_WD + '/datas/index.txt', 'r' ) as f:
            __current_index = f.read()
            
            if __current_index =='':
                id = 0
            else:
                __current_index_json = json.loads(__current_index)
                id = int(__current_index_json['Employee']) + 1
        with open(CURRENT_WD + '/datas/index.txt', 'w+' ) as f:
            f.write(json.dumps({'Employee': id}))
        return id 

    @staticmethod
    def insertEmployeeToDatabase(employee):
        data = json.dumps(employee.__dict__)
        with open(LOCAL_FILE, 'a+') as f:
            f.write(data) 
            f.write('\n')
        return True

    @staticmethod
    def insertEmployee(employee):
        if employee.ID != 0:
            return False
        employee.ID = Employee.createNewID()
        employee.Status = Status.INIT.value
        employee.DueDate = employee.DueDate.strftime("%Y-%m-%d")
        employee.CreatedAt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        employee.UpdatedAt = employee.CreatedAt
        
        return Employee.insertEmployeeToDatabase(employee)

    @staticmethod
    def getEmployeesByStatus(statuses):
        data = []
        with open(LOCAL_FILE, 'r') as f:
            data = f.readlines()
            lated_result = [] 
            looped_ids = [] 
            for i in range(len(data)-1, -1, -1):
                row = json.loads(data[i])
                if row.get('ID') not in looped_ids: 
                    lated_result.append(row)
                    looped_ids.append(row.get('ID'))
        result = [] 
        for row in lated_result: 
            if row.get('Status') in statuses or len(statuses) == 0:
                result.append(Employee.cast(row))
        return sorted(result, key=lambda row: row.ID)


    @staticmethod
    def getEmployeeByID(id):
        data = []
        with open(LOCAL_FILE, 'r') as f:
            data = f.readlines()
            result = []
            for row in data:
                row = json.loads(row)
                if row.get('ID') == id:
                    result.append(row)
            if len(result) == 0:
                return None
            return Employee.cast(result[-1])

    @staticmethod
    def getAllEmployeesByID(ids):
        data = []
        with open(LOCAL_FILE, 'r') as f:
            data = f.readlines()
            result = [] 
            looped_ids = [] 
            for i in range(len(data)-1, -1, -1):
                row = json.loads(data[i])
                if row.get('ID') not in looped_ids and row.get('ID') in ids: 
                    result.append(Employee.cast(row))
                    looped_ids.append(row.get('ID'))
            return result

    @staticmethod
    def updateEmployeeByID(employee):
        emp = Employee.getEmployeeByID(employee.ID)
        if emp is None:
            return False
        if not((emp.Status == 0 and employee.Status in (1, 2)) or (emp.Status == 2 and employee.Status == 1)):
            return False
        emp.Status = employee.Status
        emp.UpdatedAt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        emp.DueDate = emp.DueDate.strftime("%Y-%m-%d")
        emp.CreatedAt = emp.CreatedAt.strftime("%Y-%m-%d %H:%M:%S")
        return Employee.insertEmployeeToDatabase(emp)
    
# if __name__ == "__main__":
#     _new_emp = {'Name' : 'MaiAnh_abcd', 
#                 'CMND': 123456, 
#                 'Phone': 78910, 
#                 'Company': 'ABC' , 
#                 'Reason': 'new', 
#                 'DueDate': datetime.now(), 
#                 'Image': None }
    # __test_dict = { 'ID' : 7,
    #                 'Name' : 'MaiAnh_123', 
    #                 'CMND': 123456, 
    #                 'Phone': 78910, 
    #                 'Company': 'ABC' , 
    #                 'Reason': 'new', 
    #                 # 'DueDate': '2020-03-04', 
    #                 'Image': None }
    # print(Employee.insertEmployee(Employee(**_new_emp)))
    # # maianh_07 = Employee(**__test_dict)
    # print('__1', Employee.getEmployeeByID(3))
    # print('__2',Employee.getAllEmployeesByID([2,3]))
    # print('__3',Employee.getEmployeesByStatus([0,1]))
    # a = '{"ID": 3, "Name": "MaiAnh_123", "CMND": 123456, "Phone": 78910, "Company": "ABC", "Reason": "new", "DueDate": "2020-03-04", "Image": null, "Status": 2, "CreatedAt": null, "UpdatedAt": "2020-04-12 00:52:29"}'
    # print(Employee.cast(a))
