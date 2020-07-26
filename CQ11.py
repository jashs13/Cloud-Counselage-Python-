'''
CODING QUESTIONS:11
Write a Python program to get a week number.
Sample Date :
 2015, 6, 16
Expected Output :
25

'''


import datetime
print(datetime.date(2015, 6, 16).isocalendar()[1])
