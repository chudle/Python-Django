import random
import math

print("+ - * / ^ | R ! C q\n")
while True:
    op = input()
    match op:
        case "+":
            x = float(input("X - "))
            y = float(input("Y - "))
            print(x + y)
        case "-":
            x = float(input("X - "))
            y = float(input("Y - "))
            print(x - y)
        case "*":
            x = float(input("X - "))
            y = float(input("Y - "))
            print(x * y)
        case "/":
            x = float(input("X - "))
            y = float(input("Y - "))
            if y != 0:
                print(x / y)
            else:
                print("?")
        case "^":
            x = float(input("X - "))
            y = float(input("Y - "))
            print(x ** y)
        case "|":
            x = float(input("X - "))
            print(abs(x))
        case "R":
            a = float(input("A - "))
            b = float(input("B - "))
            if a <= b:
                print(random.randint(a, b))
            else:
                print("?")
        case "!":
            x = int(input("X - "))
            if x >= 0:
                print(math.factorial(x))
            else:
                print("?")
        case "C":
            x = float(input("X - "))
            if abs(x) <= 1:
                print(math.acos(x))
            else:
                print("?")
        case "q":
            break
        case default:
            print("?")
    print("")
