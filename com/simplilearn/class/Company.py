class Company:
    def __init__(self,name,id,address):
        self.name=name
        self.id = id
        self.address = address

    def details(self):
        print("My Company Name ",self.name)
        print("My Company ID ", self.id)
        print("My Company Address ", self.address)

# Creating the Object
# Inernally it will call the __init__
c1=Company("Simplilearn",101,"Bangalore")
c1.details()
