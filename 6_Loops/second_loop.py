# Exercise 2: Write another program that prompts for a list of numbers as above 
# and at the end prints out both the maximum and minimum of the numbers instead of the average.
smallest = None
largest = None

while True :
      line = input("Enter a number: ")    

      if line == 'done' :
            break
      
      try :
            number = float(line)
      
      except :
            print("Invalid input")
            continue
            
      if smallest is None or number < smallest :
            smallest = number

      if largest is None or number > largest :
            largest = number

print("Maximum is", largest)
print("Minimum is", smallest)
