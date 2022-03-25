#Requirements:
#Write a program that asks the user to input any positive integer
# and outputs the successive values of the following calculation.
#At each step calculate the next value by taking the current value and,
# if it is even, divide it by two, but if it is odd, multiply it by three and add one.
#Have the program end if the current value is one.
#$ python collatz.py
#Please enter a positive integer: 10
#10 5 16 8 4 2 1

# methods
#First, we have to make sure that the user is inserting an integer and we use the function int
n = int(input("Please enter any positive integer: ")) 

#using 'while' n>1, we make sure that the count stops at 1 and doesn't run indefinetly
while n > 1:

#below we verified if n is an odd value; and if it is we divided it by 2;
    if n % 2 == 0:
        n = n / 2
        print(n)

#with 'else' we multiplied n by 3 and we added 1;
    else:
        n = n * 3 + 1
        print(n)