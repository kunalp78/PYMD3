class Employee:
    def __init__(self, name="", age=0, address=""):
        self.name = name
        self.age = age
        self.address = address

    def __str__(self):
        return f"Name: {self.name} | \nAge: {self.age} | \nAddress: {self.address}"

    def __repr__(self):
        return f"Object(\"{self.name}\", \"{self.age}\", \"{self.address}\")"
    
    def get_attribs(self):
        print(f"Name: {self.name} | \nAge: {self.age} | \nAddress: {self.address}")


e2 = Employee("Arti", 26, address="Kerela")
print(repr(e2))
print(str(e2))
print(e2)