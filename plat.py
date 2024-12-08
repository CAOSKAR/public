import sys
print ("Skriptname: ", sys.argv[0])
from sys import platform
if platform == "linux" or platform == "linux2":
    print('System ist Linux:')
elif platform == "win32":
    print(platform)
    print('System ist Windows:')
    
