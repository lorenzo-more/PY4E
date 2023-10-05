# Exercise 1: Rewrite your pay computation to give the employee 
# 1.5 times the hourly rate for hours worked above 40 hours.
# hours = input("\nEnter Hours: ")
# rate = input("Enter Rate: ")
# hours = float(hours)
# rate = float(rate)

# if hours > 40 :
#       extra = hours % 40
#       pay = (hours * rate) + extra * (rate * 0.5)

# else :
#       pay = hours * rate

# print("Pay:", pay) # round(pay)

# Exercise 2: Rewrite your pay program using try and except 
# so that your program handles non-numeric input gracefully 
# by printing a message and exiting the program. 
hours = input("\nEnter Hours: ")
rate = input("Enter Rate: ")

try :
      hours = float(hours)
      rate = float(rate)
      

except :
      print("Error, please enter numeric input")
      quit()

if hours > 40 :
      extra = hours % 40
      pay = (hours * rate) + extra * (rate * 0.5)

else :
      pay = hours * rate

print("Pay:", pay) # round(pay)
