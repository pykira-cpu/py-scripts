
def search_string_in_file(file_name, string_to_search):
    
    """Search for the given string in file and return lines containing that string,
    along with line numbers"""

    line_number = 0
    list_of_results = []
    
    # Open the file in read only mode
    with open(file_name, 'r') as read_obj:
        
        for line in read_obj:
            line_number += 1
            if string_to_search in line:
                list_of_results.append((line_number, line.rstrip()))
    
    return list_of_results

matched_lines = search_string_in_file('filename.txt', 'madhu')

print('Total Matched lines : ', len(matched_lines))

for elem in matched_lines:
    print('Line Number = ', elem[0], ' :: Line = ', elem[1])
