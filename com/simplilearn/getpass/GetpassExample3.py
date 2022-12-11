# A simple Python program to demonstrate
# getpass.getpass() to read security question
import getpass

securityQuestion = getpass.getpass(prompt='Enter the Password? ')

if securityQuestion == 'Admin':
    print('The Password is Unlocked!')
else:
    print('You\'ve entered an invalid password!')

#https://www.javatpoint.com/getpass-module-in-python
#https://www.geeksforgeeks.org/getpass-and-getuser-in-python-password-without-echo/