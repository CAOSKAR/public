import os

file_path = "D:\\Programmierung/python"
a ='dbt run --models ' 
e =' --vars '
b ="'"
c ='{"LIEFERID" : "'
d ='"}'

for root, dirs, files in os.walk(file_path):
    for dat in files:
        
        g =(os.path.splitext(dat)[0])
        s=a+g+e+c+d+b
        print(s)