import os

fpath = "C:/temp/"
for file in os.listdir(fpath):
    basename = os.path.basename(fpath)
    file_name = os.path.join(fpath, file)
    rebasename=basename.replace('UE','Ü')
    print(os.path.join(fpath, file_name))
print(basename)
print(basename)



