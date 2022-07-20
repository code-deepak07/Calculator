a = int(input("Enter first number: "))
b = int(input("Enter next number: "))
c = input("Enter operator(+,-,*,/,%): ")
if c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
elif c == "*":
    print(a * b)
elif c == "/":
    print(a / b) 
elif c == "%":
    print(a % b) 
else:
    print("error occured")    