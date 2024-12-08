# File to open and break apart
filename = "csv_neu.csv"
filepart = filename.replace(".csv", "")
print(filepart)
fileR = open(filename, "rb")


 
part = 0
byte = fileR.read(1024000)
while byte:
    #split -l 100000 file.txt linux command to spli
    # Open a temporary file and write a chunk of bytes
    fileN = filepart + str(part) + ".csv"
    fileT = open(fileN, "wb")
    fileT.write(byte)
    fileT.close()
     
    byte = fileR.read(1024000)
    part += 1
