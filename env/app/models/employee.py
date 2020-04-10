class Employee:
    def __init__(self, Name, CMND, Phone, Company, Reason, DueDate, Image=None):
        self.ID = 0
        self.Name = Name
        self.CMND = CMND
        self.Phone = Phone
        self.Company = Company
        self.Reason = Reason
        self.DueDate = DueDate
        self.Image = Image
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