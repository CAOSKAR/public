def split_file(file_path, lines_per_file): 
    with open(file_path, 'r') as file: 
        file_number = 1 
        current_lines = [] 
        filepart = file_path.replace(".csv", "") 
        for line in file:
             
            current_lines.append(line) 
            if len(current_lines) == lines_per_file:
            #if len(current_lines) < lines_per_file:    

                with open(f'{filepart}_{file_number}.csv', 'w') as output_file: 
                    output_file.writelines(current_lines) 
                file_number += 1 
                current_lines = [] 
         
        # Write any remaining lines to a new file 
        if current_lines: 
            with open(f'{filepart}_{file_number}.csv', 'w') as output_file: 
                output_file.writelines(current_lines) 
 
# Example usage 
split_file('csv_neu.csv', 10001)  # Adjust the number of lines per file as needed 