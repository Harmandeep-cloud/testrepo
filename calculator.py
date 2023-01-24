num1 = float(input("enter number1 = "))
oper = input("enter operator")
num2 = float(input("enter number2 = "))
if oper=="+":
   print(num1+num2)
elif oper=="*":
     print(num1*num2)
elif oper=="/":
     print(num1/num2)
elif oper=="-":
     print(num1-num2)
else:
     print("invalid number or operator")