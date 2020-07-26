'''
CODING QUESTIONS:2
We add a Leap Day on February 29, almost every four years. The leap day is an extra,
or intercalary day and we add it to the shortest month of the year, February.
In the Gregorian calendar three criteria must be taken into account to identify leap
years:
● The year can be evenly divided by 4, is a leap year, unless:
● The year can be evenly divided by 100, it is NOT a leap year, unless:
● The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years,
while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.
Task
You are given the year, and you have to write a function to check if the year is a leap or
not.
Input Format
Read y, the year that needs to be checked.
Constraints
1900<_y<_10
Output Format
The output is taken care of by the template. Your function must return a boolean value
(True/False)
Sample Input
1990
Sample Output
False

'''

def check_leap(year):
	b1 = (year%100!=0) and (year%4==0)	# check for every 4 years
	b2 = (year%100==0) and (year%400==0)	# check for every 400 years
	if b1 or b2:
		return "true"
	else:
		return "false"

year = int(input("Enter year : "))
res = check_leap(year)
print(res)
