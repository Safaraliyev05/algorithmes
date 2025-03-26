import copy


class Employee:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def clone(self):
        return copy.deepcopy(self)


class EmployeeList:
    def __init__(self):
        self.employees = []

    def get(self):
        return self.employees

    def loadEmployees(self):
        self.employees.append(Employee("John", "Smith", 25))

    def cloneEmployee(self, index):
        if 0 <= index < len(self.employees):
            return self.employees[index].clone()
        return None
