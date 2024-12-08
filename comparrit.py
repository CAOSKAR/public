from comparr import comparr
import pickle
import json

sys = ['ASS_AG91','ASS_AG92','ASS_AG95','ASS_AG96','ASS_AG97']
for fina in sys:
    fina+arr1 = ('a1.csv', 'a2.csv', 'a3.csv', 'a5.csv')
    arr2 = ('a1.csv', 'a2.csv', 'a6.csv', 'a7.csv')

rs = comparr(arr1,arr2)
print ("Diese Dateien sind nicht vorhanden",rs)


rs =str(rs)
rs =str(rs.replace("'", ""))
rs =str(rs.replace(" ", ","))
dataset = rs
for fina in sys:
    outputFile = f"{fina}.data"
    with open(outputFile, 'wb') as file:
        pickle.dump(dataset, file)
        print (outputFile,dataset)

