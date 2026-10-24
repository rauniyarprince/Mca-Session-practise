# num1 =float(input("enter the number1 :"))
# num2 =float(input("enter the number2 :"))
# num3 =float(input("enter the number3 :"))
# if num1>num2 and num1>num3:
#   print("num1 is greater")
# elif num2>num1 and num2>num3:
#   print("num2 is greater")
# else:
#   print("num3 is greater")

num1 =float(input("enter the number1 :"))
num2 =float(input("enter the number2 :"))
num3 =float(input("enter the number3 :"))

if num1>num2:
  if num1>num3:
    print("num1 is greatest")
  else:
    print("num3 is greatest")
else:
  if num2 > num3:
    print("num2 is greatest")
  else:
    print("num3 is greatest")


