subject1 = float(input("Enter Subject 1 : "))
subject2 = float(input("Enter Subject 2 : "))
subject3 = float(input("Enter Subject 3 : "))
subject4 = float(input("Enter Subject 4 : "))

total = subject1 + subject2 + subject3 + subject4

average = total / 4 

print("Total : ",total)
print("Average : ",average)

if(subject1 >= 40 and subject2 >= 40 and subject3 >= 40 and subject4 >= 40) :
  print("Result : Pass")
else :
  print("Result : Fail")