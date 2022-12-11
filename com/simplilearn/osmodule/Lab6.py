"""
os.error()
The os.error() function defines the OS level errors. It raises OSError in case of invalid or inaccessible file names and path etc.
"""
import os
try:
    # If file does not exist,
    # then it throw an IOError
    filename = 'Python.txt'
    f = open(filename, 'r')
    text = f.read()
    f.close()
# The Control jumps directly to here if
# any lines throws IOError.
except IOError:
    print(os.error) #will <class 'OSError'>
    print('Problem reading: ' + filename)
