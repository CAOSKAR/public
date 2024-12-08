lst = "sda,sdb,sdc,sdd"
n = 0
for item in lst.split(","):
     print(item),
     n += 1 
if n==1:      
     print('Die Liste hat {} Wert' .format(n))
else:
     print('Die Liste hat {} Werte' .format(n))
