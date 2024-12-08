import pickle

sys = ['ASS_AG91','ASS_AG92','ASS_AG95','ASS_AG96','ASS_AG97']

# Deserialization
for fina in sys:
    outputFile = f"{fina}.data"
    with open(outputFile, 'rb') as file:
        loaded_data = pickle.load(file)
        print('Die Datei',outputFile)
        print ('hat die Werte:',loaded_data)
