import sys
print ("Skriptname: ", sys.argv[0])
if len(sys.argv) <= 1:
    print('Es wurden keine Parameter übergeben')
else: 
    for x in sys.argv[1: ]:
        print('Parameter wurde uebergeben:', x)
     




  