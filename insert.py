import os
lst = ["V_LIEFER_ID","V_LAUF_ID","SATZNUMMER","EXTRAKTIONSDATUM"]
##file_path = "D:\\Programmierung/python"
a ='INSERT INTO ' 
b ='CSV_IN'
c ='('
d ='V_LIEFER_ID,V_LAUF_ID,SATZNUMMER,EXTRAKTIONSDATUM'
e =')'
f =' VALUES'
g ='(222222,222222,111111,\'20032024\')'
#d ='"}'


##for root, dirs, files in os.walk(file_path):
for dat in lst:
        #lst.append(os.path.splitext(file)[0])
        # g =(os.path.splitext(dat)[0])
        s=a+b+c+d+e+f+g
        print(s)
#print(lst)