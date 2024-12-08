import os

file_path = "C:\\temp\SAMUNG_KUEHLSCHRANK.txt"

basename = os.path.basename(file_path)
file_name = os.path.splitext(basename)[0]+os.path.splitext(basename)[1]
file_name_1 = os.path.splitext(basename)[0]
file_name_2 = os.path.splitext(basename)[1]
print(basename)
print(file_name)
print(file_name_1)
print(file_name_2)