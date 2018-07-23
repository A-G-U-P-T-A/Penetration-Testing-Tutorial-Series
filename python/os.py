#os module usage example
import os #importing the library
print os.getcwd(),"\n" #get present working directory path
print os.stat('/usr/bin/python'),"\n" #get status of a file
print os.system('ls -la /home'),"\n" #runs shell commands
print os.chmod('test', 755),"\n" #helps change file permissions
print os.getuid(),"\n" #prints user id
print os.getgid(),"\n" #prints group id
print os.getlogin(),"\n" #get name of logged in user
print os.listdir('/home') #returns list of item present in the path specified.
#lets test the code
