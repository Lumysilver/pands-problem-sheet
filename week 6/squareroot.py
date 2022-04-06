
#We have to write a function which will return the square root of
# a number. To obtain this result we will be using the Newtons method. 
#As a source https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo
#was very useful
#Here are some methods of extracting the square root using Newton's method:
#https://math.stackexchange.com/questions/721258/newtons-method-for-estimating-square-roots




def sqrt (number) :
 
    limit = 0.00001

    # We are Assuming the sqrt of number as number only
    x = number
 
    # The number of iterations is counted.
    count = 0

 #add a counter to a while loop
    while (1) :
        count += 1
 
        # square root of a number by Newton’s Method
        root = 0.5 * (x + (number / x))
 
        # we are now verifying for closeness
        if (abs(root - x) < limit) :
            break
 
        # now we are going to update the root
        x = root
 
    return root

number = float(input("Enter a positive number: "))

#we have now entered the desired output message
print ("The square root of", number, "is approx.", sqrt(number))