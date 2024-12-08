filename = "csv_neu.csv"
filepart = filename.replace(".csv", "")
fileR = open(filename, "r")
raw = fileR.read() 
allraw = raw.split("\n") 
print('Count of raws',len(allraw)-1) 
lines = []
lines_file = 10000
finr =1
countlines = 0 
for line in fileR:
        countlines +=1
        lines.append(line)
        if len(lines) == lines_file:    
          with open(f'{filepart}_{finr}.csv', 'w') as split_file: 
            split_file.writelines(lines)
            finr += 1
            lines = []
if lines: 
          with open(f'{filepart}_{finr}.csv', 'w') as split_file: 
            split_file.writelines(lines)