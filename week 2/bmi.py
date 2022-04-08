#declare weight and height variables
#after lab 3.1 I have learned hoow to use input from comand line

weight = float(input("Enter your weight(kg): "))
height = float(input("Enter your height(cm): "))

#bmi formula found at https://www.euro.who.int/en/health-topics/disease-prevention/nutrition/a-healthy-lifestyle/body-mass-index-bmi

bmi = weight / (height/100)**2

#print the result using the fortmat function and the round function as seen in 3.1 lab
#after the round input I've noticed that the result is rounded without any decimals
#I have to modify the formula, so the result will have two decimals

print ("Your bmi is: ", round (bmi), 2)
