def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

print("Select operation:")
print("\t1. Addition")
print("\t2. Subtraction")
print("\t3. Multiplication")
print("\t4. Division")

while True:
    operation = input("Enter operation(1/2/3/4): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if operation == '1':
        print("Addition: ", add(num1, num2))
        
    elif operation == '2':
        print("Subtraction: ", sub(num1,num2))
        
    elif operation == '3':
        print("Multiplication: ",mul(num1, num2))
        
    elif operation == '4':
        print("Quotient: ", div(num1, num2))

    continue_operation = input("Do you want to continue? (yes/no): ")
    if continue_operation == "no":
        break
