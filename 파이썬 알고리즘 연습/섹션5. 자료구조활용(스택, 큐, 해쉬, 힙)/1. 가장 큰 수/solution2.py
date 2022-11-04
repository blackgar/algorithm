import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    number, m = map(int, input().split())
    n = len(str(number))
    stack = []
    # 첫번째 접근
    for i in str(number):
        tmp = 1
        if stack:
            while True:
                if stack:
                    if m == 0:
                        stack.append(i)
                        break
                    if int(stack[-tmp]) < int(i):
                        # print(stack)
                        stack.pop()
                        m -= 1
                    else:
                        stack.append(i)
                        # print("in", stack)
                        break
                else:
                    stack.append(i)
                    break
        else:
            stack.append(i)
        # print("out", stack)
    # 위 코드 리팩토링
    for i in str(number):
        while stack and m > 0 and stack[-1] < i:
            stack.pop()
            m -= 1
        stack.append(i)

    if m:
        stack = stack[:len(stack)-m]
    print(''.join(stack))
