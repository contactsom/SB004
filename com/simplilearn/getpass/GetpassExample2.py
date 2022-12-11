# A simple Python program to demonstrate
# getpass.getpass() to read security question
import getpass

securityQuestion = getpass.getpass(prompt='Your favorite Book? ')

if securityQuestion.upper() == 'JAVA':
	print('Found ..!!!')
else:
	print('The answer entered by you is incorrect..!!!')
