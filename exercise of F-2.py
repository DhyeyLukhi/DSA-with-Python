class Employee:
    def __init__(self, empid, name, salary):
        self.empid = empid
        self.name = name
        self.salary = salary
    
    def display(self):
        print(f"Employee ID: {self.empid}")
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")

E1 = Employee(101, "Alice", 50000)
E1.display()