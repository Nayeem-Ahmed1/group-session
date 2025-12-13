num1 = int(input("Enter Number 1 : "))
num2 = int(input("Enter Number 2 : "))
num3 = int(input("Enter Number 3 : "))

if(num1 > num2 and num1 > num3) :
  print("Number 1 is largest")
elif (num2 > num1 and num2 > num3) :
  print("Number 2 is largest")
else :
  print("Number 3 is Largest")

num4 = int(input("Enter Number 4 : "))

if(num4 > 0 ) :
  print("Number 4 is Positive")
elif(num4 < 0) :
  print("Number 4 is Negative")
else :
  print("Number 4 is zero")