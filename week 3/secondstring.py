#Write a program that asks a user to input a string and outputs every second 
# letter in reverse order
#text: 'The quick brown fox jumps over the lazy dog.'

#we have to assign the variable
sentence = input("Please enter a sentence: ")

#to print every second letter in reverse order had to be researched online and was found at:
#  https://stackoverflow.com/questions/28535392/what-does-n-1-means-in-python
# also [::] (double colon) is exlained at: https://www.askpython.com/python/examples/colon-in-python

print (sentence[:: -2])