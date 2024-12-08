from pathlib import Path

file_path = "C:\\temp\SAMUNG_KUEHLSCHRANK.txt"
file_name = Path(file_path).stem
print(file_name)