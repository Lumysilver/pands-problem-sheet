#this program automaticaly will tell you if 'today' is a weekday or weekend day. 
#once you run the program, youl'll have your answer.


# I have researched the topic and I have came across some valuable sources, such as: https://www.delftstack.com/howto/python/python-datetime-day-of-week/#:~:text=of%20the%20day.-,Use%20the%20weekday()%20Method%20to%20Get%20the%20Name%20of,0%20and%20Sunday%20is%206.
# The calendar library can be used in Python when the day's name is required in English. It makes use of the day_name() method, which controls an array of weekdays. Monday is at the 0th position in this array.
#I have also used as a source https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior. 

#from ast import Constant
#from datetime import date, datetime
#import calendar
#from doctest import OutputChecker
#from unittest import result
#curr_date = date.today()
#print(calendar.day_name[curr_date.weekday()])
#my_dictionary_responses = {0:calendar.MONDAY,1:calendar.TUESDAY, 2:calendar.WEDNESDAY,
#3:calendar.THURSDAY,4:calendar.FRIDAY,5:calendar.SATURDAY,6:calendar.SUNDAY}
#if (Constant) : "Monday" <= 3
 

from datetime import datetime

now = datetime.now()

zi = now.strftime("%u")

if (int(zi) > 5):
    print("It is the weekend, yay!")
else:
    print("Yes, unfortunately today is a weekday.")    


