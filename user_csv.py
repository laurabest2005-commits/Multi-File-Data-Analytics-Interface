# user_csv.py
# ENDG 233 F24
# STUDENT NAME(S)
# GROUP NAME
# A terminal-based data analysis and visualization program in Python.
# You must follow the specifications provided in the project description.
# Remember to include docstrings and comments throughout your code.

import data_files

def is_float(value):   #checks if value is a number 
    ''' Function: takes in a value, if it is a number it returns a float
    Parameters: takes value from the user
    Returns: if the value is a number then it returns the float of the value'''

    value = value.strip()

    if not value.isdigit():  #if it is not a number it doesn't change anything and returns back the value
        return value

    return float(value)  #if it is a number it returns the float of the value


def read_csv(filename, include_headers):
    '''Function: opens the csv file and reads it
    Parameters: filename is the name of the file to be read, include_headers is a flag
    for if headers should be included when the csv is read
    Returns: a 2D list of the data from the file'''

    file_list = []

    data_file = open(filename, 'r') 

    for line in data_file:

        line = line.rstrip() #strips the '\n' off of the end of the line
        row = [] #the row gets reset after each line is completed
        value = ''#the value typically gets reset after the function sees a ',' however there is no ',' after the last value in each line so we have to reset it at the start of the loop

        for char in line:   #iterate through each character in the line 
            if char == ',':
                row.append(is_float(value))  #if the character is a ',' we add the characters currently store in 'value' to the row
                value = ''   #empty 'value' so it can hold the characters for a new word/number
            else:
                value += char   #add each character in a word/number to 'value'

        row.append(is_float(value)) #empty any leftover characters from 'value' into the row
        file_list.append(row) #add the row to the final list

    if include_headers == False:
        file_list = file_list[1:]  #if no headers are required we crop the 2D list to not include the first list

    return file_list 


def write_csv(filename, data, overwrite):
    '''Function: writes the information from a csv into another csv file
    Parameters: filename is the name of the file to be written, overwrite is a flag that displays
    whether or not the data already in the file should be 'overwritten' (deleted), or not.
    Returns: none'''

    
    original_rows = []
    read_file = open(filename, 'r')

    if overwrite == False:   #if we aren't overwriting we need to know what is inside the file
        for line in read_file:
            original_rows.append(line.rstrip())  #strip the '\n' off of the end of the line and add each line to a list

    new_lines = []

    for line in data:  #for each line or embedded list in the data provided
        new_row = ''

        for value in range(len(line)): #iterate through each word/number in the line
            new_row+=str(line[value])  #add the word/number to the variable 'new_row' as a string

            if value < len(line)-1:  #unless the value is the last word/number in the line, add a coma after it
                new_row+=','

        new_lines.append(new_row) #add each completed line to the list

    
    if overwrite == True:     #if we are overwriting
        final_lines = new_lines   #the lines in the csv will be the lines only from the data that gets provided in the function
    
    if overwrite == False:   #if we are not overwriting
        final_lines = original_rows + new_lines   #we are adding the lines from the data provided to the original lines in the csv

    write_file = open(filename, 'w')

    for line in final_lines:  #for each line in our final lines, 
        write_file.write(line + '\n') #we write the line and start a new line
        



