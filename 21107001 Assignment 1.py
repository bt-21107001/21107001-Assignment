# Question1. Write a Python program to find average of three numbers entered by the user.

print("Welcome to 3 number average calculator")

number_1 = float(input("Enter 1st number "))
number_2 = float(input("Enter 2nd number "))
number_3 = float(input("Enter 3rd number "))

# Average of 3 numbers is their sum divided by 3.

average = round(((number_1 + number_2 + number_3) / 3) , 2)

print("The average is", average)


#------------------------------------------------------------------------------


#Question2. Write a python program to compute a person's income tax.

gross_income = float(input("Please enter your income.\n$"))

dependent_no = float(input("Enter number of dependents.\n"))

#standard deduction = $10,000
#dependent deduction = $3000

taxable_income = gross_income - 10000 - (dependent_no * 3000)

#Tax rate = 20%

tax_payable = round( (20 / 100 * taxable_income), 2)

if tax_payable > 0:
    print("Your income tax is $",tax_payable)
else:
    print("Your income is not eligible for taxes")


#------------------------------------------------------------------------------


# Question3. Write a program that asks the user for a number of seconds and prints out how many minutes and seconds that is.

seconds = int(input("Enter number of seconds. "))

minutes_displayed = seconds // 60

seconds_displayed = seconds % 60

print(seconds, "seconds is", minutes_displayed, "minutes and", seconds_displayed, "seconds.")


#------------------------------------------------------------------------------


# Question4. Write a python program to add three numbers 25+’25’+25.0 and produce result 75 as string.

#String '25' is coverted to integer using int function for it to be added.
#To get 75 output, we use round function on the output.

result = 25 + int('25') + 25.0

#Use string function to convert output into a string.

string_result = str(round(result))

print(string_result)


#------------------------------------------------------------------------------


# Question5. Write a program that prints out the sine and cosine of the angles ranging from 0 to 345◦ in 15◦ increments.

import math

#Since, trignmetric functions in python accept radian values,
#Input is coverted into radians
#Loop is used since we need to perform an operation over and over again

for angle in range(0, 346, 15):
    
  radian_angle = math.radians(angle)
  sine_value = math.sin(radian_angle)
  cosine_value = math.cos(radian_angle)
 
  print (round(sine_value, 4), round(cosine_value, 4))

