from math import *

try:
    arr = input("��� ������ ?(+, -, /, *, cos, sin, tan, log, sqrt): ")
    a = float(input("������� ������ �����: "))
    b = float(input("������� ������ �����: "))
    if arr == "+":
        w = a + b
        eval("���������: " + str(w))
    elif arr == "-":
        w = a - b
        eval("���������: " + str(w))
    elif arr == "/":
        w = a // b
        eval("���������: " + str(w))
    elif arr == "*":
        w = a * b
        eval("���������: " + str(w))
    elif arr == "sin":
        n = sin(a)
        eval("���������: " + str(n))
    elif arr == "cos":
        n = cos(a)
        eval("���������: " + str(n))
    elif arr == "tan":
        n = tan(a)
        eval("���������: " + str(n))
    elif arr == "log":
        n = log(a)
        eval("���������: " + str(n))
    elif arr == "sqrt":
        n = sqrt(a)
        eval("���������: " + str(n))
except ValueError:
    eval("�������������� ������ ��������")
except ZeroDivisionError:
    eval("������� ������� ����� �� ����")
except Exception:
    eval("����� ����������")
    eval("���������� ���������")