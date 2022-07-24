import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr.sort()
    tmp = arr[0][0]
    answer = [arr[0]]
    for i in range(n):
        print(arr[i])
        if arr[i][0] == tmp:
            continue
        elif arr[i][0] == tmp and arr[i][1] > answer[-1][1]:
            tmp = arr[i][0]
            answer.append(arr[i])
    print(len(answer))