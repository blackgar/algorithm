import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    calculate = list(input())
    i = 0
    stack = []
    operator = ["+", "-", "*", "/"]
    while True:
        tmp = 0
        if calculate[i] == "+":
            tmp = int(calculate[i-2]) + int(calculate[i-1])
        elif calculate[i] == "-":
            tmp = int(calculate[i - 2]) - int(calculate[i - 1])
        elif calculate[i] == "*":
            tmp = int(calculate[i - 2]) * int(calculate[i - 1])
        elif calculate[i] == "/":
            tmp = int(calculate[i - 2]) / int(calculate[i - 1])

        if calculate[i] in operator:
            calculate = calculate[:i - 2] + [tmp] + calculate[i + 1:]
            i -= 2

        if i == len(calculate)-1:
            break

        i += 1

    print(calculate[-1])