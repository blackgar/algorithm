import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    number = list(map(int, str(n)))
    stack = []

    # 스택에 넣어 비교하면서 어떤 숫자들이 남아야 하는지 비교하면서 남긴 수들을 문자열로 만들어준다.
    for i in number:
        while stack and m > 0 and stack[-1] < i:
            stack.pop()
            m -= 1
        stack.append(i)

    if m != 0:
        stack = stack[:-m]

    answer = ''.join(map(str, stack))
    print(answer)