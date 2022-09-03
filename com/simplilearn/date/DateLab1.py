import datetime
a=datetime.datetime.now()
print(a) #2022-09-03 12:30:30.128351

print(a.year) #2022
print(a.month) #9
print(a.day) #3
print(a.strftime("%A")) #Saturday
print(a.strftime("%B")) #September
print(a.strftime("%w")) #6
print(a.strftime("%d")) #03
print(a.strftime("%b")) #Sep
print(a.strftime("%m")) #09
print(a.strftime("%y")) #22
print(a.strftime("%Y")) #2022
print(a.strftime("%H")) #12
print(a.strftime("%p")) #PM