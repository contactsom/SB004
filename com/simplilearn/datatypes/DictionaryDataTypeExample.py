print("This is example of Dictionary Data type in python")

print("****** START- DICTIONARY ********")
# IT HOLD THE DATA IN KEY AND VALUE PAIR
# PHON NUMBER TO PERSON
# ACCOUNT NUMBER TO ACCOUNT HOLDER
# ROLL NUMBER TO STUDENT
# EMPLOYEE ID TO EMPLOYEE
# EMAIL ID TO STUDENT
#  Shibanijoshi94158@gmail.com -  Shibanijosh
#  manishakiran079@gmail.com -  manishakiran
#  sjnttdata@gmail.com   - sjnttdata
#  testemail@server.com - testemail

# I WANT TO CREAT THE DICTIONARY WHERE EMAIL ID AS KEY AND NAME AS VALUE

emailName={
            "Shibanijoshi94158@gmail.com":"Shibanijosh",
            "manishakiran079@gmail.com" : "manishakiran",
            "sjnttdata@gmail.com" : "sjnttdata",
            "testemail@server.com ":"testemail"
           }

print(type(emailName)) # dict
print(emailName) #{'Shibanijoshi94158@gmail.com': 'Shibanijosh', 'manishakiran079@gmail.com': 'manishakiran', 'sjnttdata@gmail.com': 'sjnttdata', 'testemail@server.com ': 'testemail'}

print("*_______________________*")

# I WANT TO CREAT THE  DICTIONARY WHERE STUDENT ROLL NUMBER AS KEY AND NAME AS VALUE

stuRollName={   1001: "Ashok",
                1002: "Suganthi",
                1003: "BettyDawn"
             }
print(type(stuRollName))
print(stuRollName)

print("****** END- DICTIONARY ********")