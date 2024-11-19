class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name  # Public attribute
        self._emp_id = emp_id  # Protected attribute
        self.__salary = salary  # Private attribute

    def set_salary(self, salary):  # Public method
        self.__salary = salary

    def get_salary(self):  # Public method accessing private data
        return self.__salary

    def _display_protected_details(self):  # Protected method
        print(f"Employee ID: {self._emp_id}")

    def display_details(self):  # Public method calling a protected one
        print(f"Name: {self.name}, Salary: {self.get_salary()}")
        self._display_protected_details()


