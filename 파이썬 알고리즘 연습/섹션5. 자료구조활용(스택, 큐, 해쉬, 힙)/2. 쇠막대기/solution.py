import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    arr = list(input())
    stack = []
    cnt = 0
    for i in range(len(arr)):
        if arr[i] == "(":
            stack.append(arr[i])
        # 닫는 괄호 만났을 때
        else:
            # 스택에 여는 괄호가 있어야 pop하고 그 길이 측정가능
            stack.pop()
            if arr[i-1] == '(':
                cnt += len(stack)
            else:
                cnt += 1
            # 만약 스택에 아무것도 없으면 그냥 다시 돌기
        # print(stack)
        # print(cnt)

    print(cnt)