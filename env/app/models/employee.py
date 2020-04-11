import json
import datetime
import os
CURRENT_WD = os.path.dirname(os.path.realpath(__file__))
LOCAL_FILE = CURRENT_WD + 'datas/database.csv'

class Employee:
    def __init__(self, Name):
        self.ID = 0
        self.Name = Name
        self.Status = 0
        self.CreatedAt = None
        self.UpdatedAt = None

    @staticmethod
    def createNewID():
        with open('index.txt', 'w' ) as f:
            data = f.read()
            if data is None:
                id = 0
            else:
                id = int(data) + 1
            f.write(id)
            f.close()
        return id 

    @staticmethod
    def insert(employee):
        if employee.ID != 0:
            return False
        employee.ID = self.createNewID()
        employee.Status = Status.INIT
        data = json.dumps(employee.__dict__)
        with open(LOCAL_FILE, 'a+') as f:
            f.write(data)
            f.close()    
        return True

    # thêm CreatedAt 
    @staticmethod
    def getEmployeesByStatus(status):
        with open(LOCAL_FILE, 'r') as f:
            data = f.read()
            result  = [] 
            for row in data: 
                if row.get(Status) = status:
                    result.append(row)
        return result
    
    @staticmethod
    def updateEmployeeByID(employee):
        return employee.ID

# thêm updated at 
    @staticmethod
    def getEmployeeByID(id):
        r = Employee('')
        return r

