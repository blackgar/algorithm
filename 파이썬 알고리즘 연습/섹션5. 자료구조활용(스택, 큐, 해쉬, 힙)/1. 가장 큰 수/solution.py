import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    number = list(map(int, str(n)))
    stack = []

    for i in number:
        while stack and m > 0 and stack[-1] < i:
            stack.pop()
            m -= 1
        stack.append(i)

    if m != 0:
        stack = stack[:-m]

    answer = ''.join(map(str, stack))
    print(answer)