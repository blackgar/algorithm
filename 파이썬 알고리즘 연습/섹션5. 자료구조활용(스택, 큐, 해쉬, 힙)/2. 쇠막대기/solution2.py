import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    braces = input()
    n = len(braces)
    stack = []
    answer = 0

    for i in range(n):
        if braces[i] == "(":
             stack.append(braces[i])
        elif braces[i] == ")":
            if braces[i-1] == "(":
                stack.pop()
                answer += len(stack)
            elif braces[i-1] == ")":
                stack.pop()
                answer += 1
    print(answer)