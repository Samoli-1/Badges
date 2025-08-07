class Customer:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        print(self.name, self.gender)

def info(customer):
    if customer.gender == "male":
        print(f"HELLO, {customer.name}, sir")
    elif customer.gender == "female":
        print(f"HELLO, {customer.name}, Ma'am")
    else:
        print(f"HELLO {customer.name}, Transgender")

namee = input("Enter Your Name : ")
genderr = input("Enter Your Gender : ")

obj = Customer(namee, genderr)
obj2 = info(obj)