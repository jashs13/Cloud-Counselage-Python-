'''
CODING QUESTIONS:7
Write a Python program to convert temperatures to and from celsius, Fahrenheit.
[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in
Fahrenheit ]
Expected Output :
60°C is 140 in Fahrenheit
45°F is 7 in Celsius

'''

fah = float(input("Enter temp in fah : "))
cel = (fah-32)*5/9
fah = round(fah,2)
cel = round(cel,2)
print(cel , "degree C is " , fah , " in Fahrenheit.")
print(fah , "degree F is " , cel , " in Celsius.")