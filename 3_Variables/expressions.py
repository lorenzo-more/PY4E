# Exercise 2: Write a program that uses input to prompt a user for their name and then welcomes them.
name = input("Enter your name: ")
print("Hello", name)

# Exercise 3: Write a program to prompt the user for hours and rate per hour to compute gross pay.
hours = input("\nEnter Hours: ")
rate = input("Enter Rate: ")
pay = float(hours) * float(rate)
print("Pay:", pay) # round(pay)

# Exercise 5: Write a program which prompts the user for a Celsius temperature, 
# convert the temperature to Fahrenheit, and print out the converted temperature.
temp_c = input("\nEnter temperature in Celsius: ")
temp_f = (float(temp_c) * (9 / 5) ) + 32
print("Temperature in Fahrenheit:", temp_f)

# Extra: converting from Fahrenheit to Celsius
f_temp = input ("\nEnter temperature in Fahrenheit: ")
c_temp = (float(f_temp) - 32 ) * (5 / 9)
print("Temperature in Celsius:", c_temp)
