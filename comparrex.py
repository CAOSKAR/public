from comparr import comparr
import pickle

arr1 = ('a1.csv', 'a2.csv', 'a3.csv', 'a5.csv')
arr2 = ('a1.csv', 'a2.csv', 'a6.csv', 'a7.csv')
sys = 'ASS_AG91'
rs = comparr(arr1,arr2)
print ("Diese Dateien sind nicht vorhanden",rs)
#rs = tuple(map(tuple,rs))
print (type(rs))
print(rs)
#for va in rs:
rs =str(rs)
rs =str(rs.replace("'", ""))
dataset = rs
outputFile = f"{sys}.data"
fw = open(outputFile, 'wb')
pickle.dump(dataset, fw)
fw.close()   
print (dataset)