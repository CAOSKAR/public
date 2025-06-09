stored_files = ['file_20241201', 'file_20241202', 'file_20241203',
                        'file_20241204', 'file_20241205', 'file_20241206','file_20241208', 'file_20241209', 'file_20241210'
                        ,'file_20241211', 'file_20241212', 'file_20241213','file_20241214', 'file_20241215', 'file_20241216']

added_files = ['file_20241201', 'file_20241202', 'file_20241207']

for file in added_files:
    if file in stored_files:
        print(f"######### CHECK FILE ##########")
        print(f" {file} is available.")
    else:
        print(f"######### CHECK FILE ##########")
        print(f" {file} is not available, {file} will be added .")
        stored_files.append(file)
        print(stored_files)
        
print(f"###############################")
print("\nFiles are comapred!")