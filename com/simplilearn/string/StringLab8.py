print("This is example is for String if operator - Lab-8 in python")
print("****** START- STRING if OPERATOR ********")

myName="Anuj Kumar"
if "Anuj" in myName:
    print("Anuj Exist")
print("__________________________")

myName1="Anuj Kumar Mayur"
if "BettyDawn" in myName1: # false
    print("BettyDawn Exist")
else:
    print("BettyDawn NOT Exist")

print("________________________")

myName2="Anuj Kumar Mayur"
if "BettyDawn" in myName2: # false
    print("BettyDawn Exist")
print("I am neither if nor else")

print("--------------------------")

myName3="Anuj Kumar Mayur"
if "Mayur" in myName3: # true
    print("BettyDawn Exist")
print("I am neither if nor else")

print("--------------------------")
#myName4="Anuj Kumar Mayur"
#if Mayur in myName4: # Against the syntex of if... in operator
 #   print("BettyDawn Exist")
#print("I am neither if nor else")





print("****** END- STRING if OPERATOR ********")