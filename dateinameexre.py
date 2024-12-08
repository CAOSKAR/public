import os

file_path = "C:\\temp\SAMUNG_KUEHLSCHRANK.txt"

basename = os.path.basename(file_path)
file_name = os.path.splitext(basename)[0]+os.path.splitext(basename)[1]
rebasename=basename.replace('UE','Ü')

print(basename)
print(rebasename)
print(file_name)

