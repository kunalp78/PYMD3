class Employee:
    def __init__(self, name="", age=0, pos="", address="", salary=0):
        self.__name = name
        self.__age = age
        self.__address = address
        self.__salary = salary
        self.__position = pos

    def set_name(self, name):
        """
        This method is responsible for seeting the name for the instance
        """
        self.__name = name

    def get_name(self):
        return self.__name

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_pos(self, pos):
        self.__position = pos

    def get_pos(self):
        return self.__position

    def set_address(self, addr):
        self.__address = addr
    
    def get_address(self):
        return self.__address

    def get_salary(self):
        return self.__salary
    
    def set_salary(self, salary):
        self.__salary = salary

e1 = Employee()
# print(e1.get_name())

e1.set_name("Divyam")
e1.set_age(25)
e1.set_address("Maharastra")
e1.set_salary(58000000)
e1.set_pos("employee")

print(e1.get_name())
print(e1.get_salary())