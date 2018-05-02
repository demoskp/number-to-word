class Employee(object):

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self,first,last,pay):
        self._first = first
        self._last = last
        self._pay = pay

        Employee.num_of_emps += 1               # Not Using self and instead using Employee in order to update the class variable and not the instance variable

    def get_full_name(self):
        return "{} {}" .format (self._first , self._last)    

    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls,str_1):
        first , last , pay = str_1.split('/')
        return cls(first,last,pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
             return False   

class Developer(Employee):
    def __init__(self,first,last,pay,prog_language):
        super().__init__(first,last,pay)  
        self.prog_language = prog_language      


class Manager(Employee):
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees    

    def add_emp(self,emp):
        self.employees.append(emp)   

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def show_emp(self):
        for employee in self.employees:
            print ('-->', employee.get_full_name()) 

    

dev_1 = Developer('Demos','Petsas',40000,'Python')        

Employee.raise_amount = 1.05

employee_2 = Employee.from_string('Andres/Prs/40000')

manager_1 = Manager('John','Batchelor',75000,[dev_1])

import datetime
my_date = datetime.date(2016,7,11)

# print(Employee.is_workday(my_date))
# print(employee_2.get_full_name())
# print(employee_2._pay)

# manager_1.show_emp()

print(isinstance(Developer,object))