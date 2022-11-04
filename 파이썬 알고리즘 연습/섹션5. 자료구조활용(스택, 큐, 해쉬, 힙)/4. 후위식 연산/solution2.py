import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    # calculate = list(input())
    calculate = input()
    i = 0
    stack = []
    operator = ["+", "-", "*", "/"]
    # stack이 아닌 풀이 방법
    # while True:
    #     tmp = 0
    #     if calculate[i] == "+":
    #         tmp = int(calculate[i-2]) + int(calculate[i-1])
    #     elif calculate[i] == "-":
    #         tmp = int(calculate[i - 2]) - int(calculate[i - 1])
    #     elif calculate[i] == "*":
    #         tmp = int(calculate[i - 2]) * int(calculate[i - 1])
    #     elif calculate[i] == "/":
    #         tmp = int(calculate[i - 2]) / int(calculate[i - 1])
    #
    #     if calculate[i] in operator:
    #         calculate = calculate[:i - 2] + [tmp] + calculate[i + 1:]
    #         i -= 2
    #     if i == len(calculate)-1:
    #         break
    #
    #     i += 1
    #
    # print(calculate[-1])

    # stack으로 푼 방법
    for x in calculate:
        if x.isdecimal():
            stack.append(x)
        else:
            tmp1 = int(stack.pop())
            tmp2 = int(stack.pop())
            if x == "+":
                stack.append(tmp2 + tmp1)
            elif x == "-":
                stack.append(tmp2 - tmp1)
            elif x == "*":
                stack.append(tmp2 * tmp1)
            elif x == "/":
                stack.append(tmp2 / tmp1)

    print(stack)