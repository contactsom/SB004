class Student:
    def setName(self,name):
        self.name=name

    def getName(self):
        return self.name

    def setMarks(self,marks):
        self.marks=marks

    def getMarks(self):
        return self.marks

n=int(input('Enter the number of students:'))
for i in range(n):
    s = Student()

    name=input('Enter the name of students:')
    s.setName(name)

    marks = input('Enter the Marks of students:')
    s.setMarks(marks)

    print("Hi ",s.getName())
    print("Your Marks is ",s.getMarks())




