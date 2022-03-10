#declare weight and height variables
#after lab 3.1 I have learned hoow to use input from comand line

weight = float(input("Enter your weight"))
height = float(input("Enter your height"))

#bmi formula found at https://www.w3resource.com/python-exercises/python-basic-exercise-66.php

bmi = weight / (height/100)**2

#print the result using the fortmat function and the round function as seen in 3.1 lab
print ("Your bmi is: ", round (bmi))git 
