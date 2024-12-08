lst = [10200,20200,30200,50200,80200,12333,14333]
a ='dbt run --models DEINMODELL --vars '
b ="'"
c ='{"LIEFERID" : "'
d ='"}'
for i in lst:
  s=a+b+c+str(i)+d+b
  print(s)
 
 