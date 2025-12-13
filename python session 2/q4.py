marks = int(input("Enter Marks (0-100) : "))

if(marks >= 80 and marks <= 100) :
  print("A")
elif(marks >= 70 and marks < 80) :
  print("B")
elif(marks >= 60 and marks < 70) :
  print("C")
elif(marks >= 50 and marks < 60) :
  print("D")
else :
  print("Fail")