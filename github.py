from math import *

try:
    arr = input("Что делаем ?(+, -, /, *, cos, sin, tan, log, sqrt): ")
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    if arr == "+":
        w = a + b
        print("Результат: " + str(w))
    elif arr == "-":
        w = a - b
        print("Результат: " + str(w))
    elif arr == "/":
        w = a // b
        print("Результат: " + str(w))
    elif arr == "*":
        w = a * b
        print("Результат: " + str(w))
    elif arr == "sin":
        n = sin(a)
        print("Результат: " + str(n))
    elif arr == "cos":
        n = cos(a)
        print("Результат: " + str(n))
    elif arr == "tan":
        n = tan(a)
        print("Результат: " + str(n))
    elif arr == "log":
        n = log(a)
        print("Результат: " + str(n))
    elif arr == "sqrt":
        n = sqrt(a)
        print("Результат: " + str(n))
except ValueError:
    print("Преобразование прошло неудачно")
except ZeroDivisionError:
    print("Попытка деления числа на ноль")
except Exception:
    print("Общее исключение")
    print("Завершение программы")