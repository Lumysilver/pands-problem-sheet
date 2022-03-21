#messing with bolean
#Author: Andrew Beatty

if False:
    #statments
    print("condition is true")
b = 3
if b == 2:
    print("b is equal to 2")
else:
    print("I hoppe this is not displayed")

if 2 != 3:
    print("I hope this is not dispayed!")
else:
    print("2 is not equal to 2 is false")

#check if something is even
aNumber = 5
if (aNumber % 2) == 0:  #we don't necessarly need the brackets, are here only for clarity
    print (aNumber, " is even") #another way of printing variables
elif(aNumber % 3) == 0: #if the number is even, this will not be checked
    print(aNumber, " is divisable by 3")
else:
    print(aNumber, " is not even or divisable by 3")

    print("this will always be outputted")