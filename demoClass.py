class DemoClass:
    # constructor
    def __init__(self):
        # initializing instance variable
        self.num=100

    # a method
    def read_number(self):
        print(self.num)


# creating object of the class. This invokes constructor
obj = DemoClass()

# calling the instance method using the object obj
obj.read_number()