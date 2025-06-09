def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

operation = input("Enter operation (+, -, *, /): ")
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

result = operations[operation](x, y)
print(result)