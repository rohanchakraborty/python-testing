def div(dividend,divisor):
  # errors are often used as flow control as if statements
  if divisor == 0:
    raise ZeroDivisionError("divisor is 0, and it can't be") #ValueError,RunTimeError...
   
  #if divisior ==0:
   # print("go do a mathematics refresher")
    #return
  ##or
    
   return dividend/divisor
students = [
  {"name":"Rob", "grades":[75,90]}
  {"name":"Bob", "grades":[]}
try:
  for student in students:
    name = student["name"]
    grades = student["grades"]
    av = divide(sum(grades),len(grades))
    print(f"{name} averaged {av}.")
except ZeroDivisionError:
  print("Error: {name} has no grades") # in case of an error
else:  
  print(f"grades calculation done") 
finally:
  print("Game over")

