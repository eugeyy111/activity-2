class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary >= 0:
            self.__salary = new_salary
        else:
            print("Invalid salary.")

# Usage
employee = Employee("mickey", 400000)
print("Employee name:", employee.get_name())
print("Employee salary:", employee.get_salary())
employee.set_salary(600000)
print("Updated salary:", employee.get_salary())
