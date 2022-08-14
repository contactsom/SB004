print("This is example is for String Formatting - Lab-10 in python")
print("****** START- STRING Formatting ********")

simplilearnheading= ' 3,000,000 careers advanced '
print(simplilearnheading)
print("___________________________________________________________")

print(' %(careersvalue)d careers advanced '
        %{"careersvalue":3000000}
      )

# SIMPLILEARN is INDIA no 1 PYTHON training portal

print(' %(edtech)s is %(country)s no %(rank)d %(course)s training portal '
      % {"edtech": "SIMPLILEARN","country":"INDIA","rank":1,"course":"PYTHON"}
      )

#1,500 live classes every month
simplilearntag="{} live classes  every month"
cources=1500
print(simplilearntag.format(cources))

print("__________________________________")
simplinewtag="{edtech} is {country} no {rank} {course} training portal"
print(simplinewtag.format(edtech= "SIMPLILEARN",country="INDIA",rank=1,course="PYTHON"))


print("****** END- STRING Formatting ********")