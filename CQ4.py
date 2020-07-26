'''
CODING QUESTIONS:4
Little Robert likes mathematics. Today his teacher has given him two integers and
asked to find out how many integers can divide both the numbers. Would you like to
help him in completing his school assignment?
Input Format :
There are two integers, a and b as input to the program.
Output Format:
 Print the number of common factors of a and b. Both the input value should be in a
range of 1 to 10^12.
Input:
10
15
Output:
2

'''


num1 = int(input("Enter the first num : "))
num2 = int(input("Enter the second num : "))

num1_factors, num2_factors = [],[]

# find factors of num1
for i in range(1,num1+1):
	if(num1 % i == 0):
		num1_factors.append(i)
print(num1_factors)
		
# find factors of num2
for i in range(1,num2+1):
	if(num2 % i == 0):
		num2_factors.append(i)
print(num2_factors)

########### common ##############
num1_set = set(num1_factors)
#print(num1_set)

num2_set = set(num2_factors)
#print(num2_set)

common = num1_set & num2_set
print("Common factors : ", common, "\t Number of common factors : ", len(common))







