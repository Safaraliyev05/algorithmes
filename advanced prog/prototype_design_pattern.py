# import copy
#
#
# class Employee:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#     def clone(self):
#         return copy.deepcopy(self)
#
#
# class EmployeeList:
#     def __init__(self):
#         self.employees = []
#
#     def get(self):
#         return self.employees
#
#     def loadEmployees(self):
#         self.employees.append(Employee("John", "Smith", 25))
#
#     def cloneEmployee(self, index):
#         if 0 <= index < len(self.employees):
#             return self.employees[index].clone()
#         return None
class Address:
    def __init__(self, street, city, state):
        self.street = street
        self.city = city
        self.state = state

    def clone(self):
        return Address(self.street, self.city, self.state)

    def __repr__(self):
        return f"Address({self.street}, {self.city}, {self.state})"


class Employee:
    def __init__(self, f_name, l_name, age):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.addresses = []

    def add_address(self, street, city, state):
        self.addresses.append(Address(street, city, state))

    def clone(self):
        emp_clone = Employee(self.f_name, self.l_name, self.age)
        emp_clone.addresses = [addr.clone() for addr in self.addresses]
        return emp_clone

    def __repr__(self):
        return f"Employee({self.f_name}, {self.l_name}, {self.age}, {self.addresses})"


class EmployeeService:
    def __init__(self):
        self.employees = []

    def add_employee(self, f_name, l_name, age):
        employee = Employee(f_name, l_name, age)
        self.employees.append(employee)
        return employee

    def __repr__(self):
        return f"EmployeeService({self.employees})"
