import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    result = 0

    for i in range(n):
        if arr[i] == 1:
            cnt += 1
            result += cnt
        else:
            cnt = 0
    print(result)