# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime 
# and create a function called computepay which takes two parameters (hours and rate).

def computepay(hours, rate) :
      try :
            hours = float(hours)
            rate = float(rate)
      
      except :
            print("Error, please enter numeric input")
            quit()

      if hours > 40 :
            extra = hours % 40
            return (hours * rate) + extra * (rate * 0.5)

      else :
            return hours * rate
      
hours = input("\nEnter Hours: ")
rate = input("Enter Rate: ")
print("Pay:", computepay(hours, rate))
