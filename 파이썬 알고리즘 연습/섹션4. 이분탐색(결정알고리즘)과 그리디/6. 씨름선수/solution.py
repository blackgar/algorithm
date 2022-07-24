import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    for i in range(n):
        flag = True
        for j in range(n):
            if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
                flag = False
                break
        if flag:
           cnt += 1
    print(cnt)