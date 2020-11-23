class Employee:
    stream = "cse"

    def __init__(self, id):
        self.id = id
        print("employee created for id", self.id)

    def __init__(self, id, name):
        self.id = id
        self.name = name
        print("Employee created for id and name", self.id, self.name)


obj1 = Employee(1, 'upendra')
obj2 = Employee(2, 'deepa')
obj3 = Employee(1)
print(Employee.stream)
