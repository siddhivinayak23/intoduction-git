'''Write a python program to accept two integers and check whether they are equal or not.
Test Data : 15 15
Expected Output :
Number1 and Number2 are equal'''

Number1 = int(input("Enter your First NO: "))
print(f"Your first no is {Number1}")
Number2 = int(input("Enter your second NO: "))
print(f"Your second no is {Number2}")

if Number1 == Number2:
  print("Number1 and Number2 are equal")
else:
  print("Number1 and Number2 are not equal")
