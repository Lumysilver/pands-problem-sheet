#I have created a textfile called moby-dick.txt where I've added a text copied 
#from Wikipedia about Moby Dick
#References: https://www.w3schools.com/python/python_file_open.asp
#           https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/

#Take the input from the comandline
text_file = str(input("Enter the file name here: "))

#now we are opening the file
open_file = open (text_file)

#read the file content
file_content = (open_file.read())

#count how many times the letters "e" appears. 
print (file_content.count("e"))


