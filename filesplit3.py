
import glob
from filesplit.split import Split

filels = glob.glob("tosplit/*.csv")
for filename in filels:
    fileR = open(filename , "r")
    outdir= 'split/'
    raw = fileR.read() 
    allraw = raw.split("\n") 
    print('Count of raws',filename,len(allraw)-1) 
    lines_file = 10000
    Split(filename,outdir).bylinecount(lines_file)
