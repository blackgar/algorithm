import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    calculate = input()
    plus_minus = ["+", "-"]
    mul_div = ["*", "/"]
    stack = []
    res = ""

    for x in calculate:
        if x.isdecimal():
            res += x
        else:
            if x == "(":
                stack.append(x)
            elif x in mul_div:
                while stack and stack[-1] in mul_div:
                    res += stack.pop()
                stack.append(x)
            elif x in plus_minus:
                while stack and stack[-1] != "(":
                    res += stack.pop()
                stack.append(x)
            elif x == ")":
                while stack and stack[-1] != "(":
                    res += stack.pop()
                stack.pop()

    while stack:
        res += stack.pop()

    print(res)
