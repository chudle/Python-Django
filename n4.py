import random
import math

print("+ - * / ^ | R ! C\n")
while True:
    op = input()
    match op:
        case "+":
            print("X - ", end='')
            x = float(input())
            print("Y - ", end='')
            y = float(input())
            print(x + y)
        case "-":
            print("X - ", end='')
            x = float(input())
            print("Y - ", end='')
            y = float(input())
            print(x - y)
        case "*":
            print("X - ", end='')
            x = float(input())
            print("Y - ", end='')
            y = float(input())
            print(x * y)
        case "/":
            print("X - ", end='')
            x = float(input())
            print("Y - ", end='')
            y = float(input())
            if y != 0:
                print(x / y)
            else:
                print("?")
        case "^":
            print("X - ", end='')
            x = float(input())
            print("Y - ", end='')
            y = int(input())
            f = 0
            if y < 0:
                y = abs(y)
                f = 1
            r = 1
            i = 0
            while i < y:
                r = r * x
                i = i + 1
            if f == 1:
                print(1 / r)
            else:
                print(r)
        case "|":
            print("X - ", end='')
            x = float(input())
            print(abs(x))
        case "R":
            print("A - ", end='')
            a = int(input())
            print("B - ", end='')
            b = int(input())
            if a <= b:
                print(random.randint(a, b))
            else:
                print("?")
        case "!":
            print("X - ", end='')
            x = float(input())
            i = 1
            j = 1
            if x > 0:
                while i <= x:
                   j = j * i
                   i = i + 1
            else: 
                i = i - 2
                while i >= x:
                   j *= i
                   i -= 1
            print(j)
        case "C":
            print("X - ", end='')
            x = float(input())
            print(math.acos(x))
        case default:
            print("?")
    print("")
