# Exercise 1: Write a program which repeatedly reads numbers until the user enters “done”. 
# Once “done” is entered, print out the total, count, and average of the numbers. 
# If the user enters anything other than a number, detect their mistake using try and except and 
# print an error message and skip to the next number.
sum = 0.0
count = 0

while True :
      line = input("Enter a number: ")
      
      if line == 'done' :
            break
      
      try :
            number = float(line)
      
      except :
            print("Invalid input")
            continue

      sum = sum + number
      count = count + 1
      
print("Sum:", sum, "Count:", count, "Average:", sum / count)
