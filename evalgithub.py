from math import *

try:
    arr = input("Что делаем ?(+, -, /, *, cos, sin, tan, log, sqrt): ")
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    if arr == "+":
        w = a + b
        eval("Результат: " + str(w))
    elif arr == "-":
        w = a - b
        eval("Результат: " + str(w))
    elif arr == "/":
        w = a // b
        eval("Результат: " + str(w))
    elif arr == "*":
        w = a * b
        eval("Результат: " + str(w))
    elif arr == "sin":
        n = sin(a)
        eval("Результат: " + str(n))
    elif arr == "cos":
        n = cos(a)
        eval("Результат: " + str(n))
    elif arr == "tan":
        n = tan(a)
        eval("Результат: " + str(n))
    elif arr == "log":
        n = log(a)
        eval("Результат: " + str(n))
    elif arr == "sqrt":
        n = sqrt(a)
        eval("Результат: " + str(n))
except ValueError:
    eval("Преобразование прошло неудачно")
except ZeroDivisionError:
    eval("Попытка деления числа на ноль")
except Exception:
    eval("Общее исключение")
    eval("Завершение программы")