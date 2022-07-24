import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    n = 7
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr_reverse = [x for x in zip(*arr)]
    cnt = 0

    for i in range(n):
        for j in range(n-4):
            tmp = arr[i][j:j+5]
            if tmp == tmp[::-1]:
                cnt += 1
        for j in range(n-4):
            tmp = arr_reverse[i][j:j+5]
            if tmp == tmp[::-1]:
                cnt += 1
    print(cnt)