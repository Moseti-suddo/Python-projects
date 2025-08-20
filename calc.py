#Simple Python calculator


operator = input("Enter one operator (+, -, *, /): ")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

try:
    if operator == "+" :
        result = num1 + num2
        print(result) 
   
    elif operator == "-" :
       result = num1 - num2
       print(result) 

    elif operator == "*" :
       result = num1 * num2
       print(result) 
    elif operator == "/" :
       result = num1 / num2
       print(round(result, 3)) #rounding up the result to 3dp

    else :
        print(f'{operator} is not a valid operator')
except ZeroDivisionError as f:
    print(f"error {f}")   