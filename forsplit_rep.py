d ='V_LIEFER_ID,V_LAUF_ID,SATZNUMMER,EXTRAKTIONSDATUM,'
d=d.rstrip(",")
i=0
for k in d.split(","):
    i=i+1      
    print(i,k)