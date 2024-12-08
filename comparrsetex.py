from comparrset import comparrset
import pickle
import json

sys = ['ASS_AG91','ASS_AG92','ASS_AG95','ASS_AG96','ASS_AG97']

for fina in sys:
    arr1 = ('a1.csv', 'a2.csv', 'a3.csv', 'a5.csv')
    arr2 = ('a1.csv', 'a2.csv', 'a6.csv', 'a7.csv')
    fi = comparrset(arr1,arr2)
    rs =str(fi)
    rs =rs.replace("'", "")
    dataset = rs
    outputFile = f"{fina}.data"
    with open(outputFile, 'wb') as file:
        pickle.dump(dataset, file)
        print (outputFile,dataset)
