name = input("What is your name? ")
print ("Hello " + name)

num1 = float(input("Enter First Number: "))  #float bcuz user can only type number
op = (input("Enter Operator: "))
num2 = float(input("Enter Second Number: "))

if op == "+":           # == bcuz thats the value of the input and the = is not assigned
    print (num1 + num2)
elif op == "-":
    print (num1 - num2)
elif op == "/":
    print (num1 / num2)
elif op == "*":
    print (num1 * num2)
else:
    print ("Invalid Operator try another one")


