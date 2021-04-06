from collections import Counter

import pyperclip
# FILE HANDLING IN PYTHON
# TO OPEN FILES: we use the function open(filename, mode)
"""
   filename = name of the file
   mode = r, w, rw
   r = read mode => Allows us to read data from the file and not any other thing
   w = write mode => Allows users to add data to the file
   + = readwrite mode (Updating) => Allows us to read and write data inorder to update the file contents
   a  = append mode => The pointer is at the end of the file and will add data without deleting the file contents
   x  = Opens a file for exclusive creation. If the file already exists, the operation fails.
"""

# Here we're opening the file in read mode then reading the file contents and printing it
"""
    file = open("errorMssgs.txt", 'r')
    readfile = file.read()
    print(readfile)
"""
# Safer way of doing this
try:
    file = open("errorMssgs.txt", 'r')
    readfile = file.readline()
    print(readfile)
    file.close()
except FileNotFoundError as e:
    print(e)


# Writing files Create new files and write into them
def create_and_writefile_newfiles(namefile, message):
    try:
        with open(namefile+".py", 'x') as file1:
            readf1 = file1.write(message)
            print(readf1, end=" ")
    except FileExistsError as error0:
        print(error0)


# create_and_writefile_newfiles("file00", "print('Coding is bae')")


def create_and_writefile_to_existing_files(namefile, message):
    try:
        with open(namefile+".txt", 'a') as file1:
            readf1 = file1.write(message)
            print(f"{readf1} \n")
    except FileExistsError as error0:
        print(error0)


# create_and_writefile_to_existing_files("file119", "Added another line through append")


# Let's now count words in a list
def count_words_in_file(file_name):
    try:
        with open(file_name, 'r') as f:
            data = f.read()
            word_list = data.split()
            no_of_words = len(word_list)
            print(no_of_words)
    except Exception as error_1:
        print(error_1)


# count_words_in_file("file11.py")


# Task 2 : Count the number of occurrences of a word in each file
def count_word_occurrence_in_file(file_name):
    try:
        with open(file_name, 'r') as file1:
            read_file = file1.read()
            word_list = read_file.split()
            each_word_occurrence = Counter(word_list)
            print(each_word_occurrence)

    except Exception as error:
        print(error)


count_word_occurrence_in_file("file119.txt")

