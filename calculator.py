def summa(a, b):
    return a + b
def minus(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
a = int(input("Первое число: "))
b = int(input("Второе число: "))
op = input("Операции (+, -, *, /): ")
if op == "+":
    print("Результат: ",summa(a, b))
elif op == "-":
    print("Результат: ",minus(a, b))
elif op == "*":
    print("Результат: ",multiply(a, b))
elif op == "/":
    if b == 0:
        print("На нуль делить нельзя!")
    else:
        print("Результат: ",divide(a, b))
else:
    print("Неизвестная операция!")
