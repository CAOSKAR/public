import os
#lst = []
file_path = "D:\\Programmierung/python"
a ='dbt run --models ' 
e =' --vars '
b ="'"
c ='{"LIEFERID" : "'
d ='"}'


for root, dirs, files in os.walk(file_path):
    for dat in files:
        #lst.append(os.path.splitext(file)[0])
        g =(os.path.splitext(dat)[0])
        s=a+g+e+c+d+b
        print(s)
#print(lst)
