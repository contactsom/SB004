print("This is example for LOG 2 in python")
print("****** START- LOG ********")
import logging

logging.basicConfig(filename="mylog.log", level=logging.INFO)
try:
    x = int(input("Enter First Number: "))
    y = int(input("Enter Second Number: "))
    print(x/y)
except ZeroDivisionError as msg1:
    print("Ca't Divide with Zero")
    logging.exception(msg1)
except ValueError as msg2:
    print("Please provide the Int value only")
    logging.exception(msg2)
logging.info("Your Task is done")
