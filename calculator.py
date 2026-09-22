print:("welcome to yasintoby's arithemetic calculator")
num1, sign, num2 = input("Enter your equation: ").split()
x= float(num1)
y= float(num2)
if sign == "+" :
    value=(x + y)
    print(value)
elif sign == "-" :
    value=(x - y)
    print(value)
elif sign == "*" :
    value=(x * y)
    print(value)
elif sign == "/" :
    value= (x / )
    print(value)
else:
    print(Error, invalid equation)
