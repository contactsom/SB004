# Import Module
import ftplib

# Fill Required Information
HOSTNAME = "tp.dlptest.com"
USERNAME = "dlpuser@dlptest.com"
PASSWORD = "ck5yS1lUWDlnN3ozUmdKUm14V3VHSGJldQ"

# Connect FTP Server
print('START-Connect FTP Server')
ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)
print('END-Connect FTP Server')

# force UTF-8 encoding
ftp_server.encoding = "utf-8"

# Enter File Name with Extension
filename = "abc.txt"

# Read file in binary mode
with open(filename, "rb") as file:
	# Command for Uploading the file "STOR filename"
	ftp_server.storbinary(f"STOR {filename}", file)

# Get list of files
ftp_server.dir()

# Close the Connection
ftp_server.quit()
