class Employee:
    def __init__(self, Name):
        self.ID = 0
        self.Name = Name
        self.Status = 0

    @staticmethod
    def insert(employee):
        return 0
    
    @staticmethod
    def getEmployeesByStatus(status):
        return []
    
    @staticmethod
    def updateEmployeeByID(employee):
        return employee.ID

    @staticmethod
    def getEmployeeByID(id):
        r = Employee('')
        return r