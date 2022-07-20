import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    n = 9
    m = 9
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr_reverse = []

    for i in zip(*arr):
        arr_reverse.append(i)
    isYes = 1

    number = list(x for x in range(1, 10))

    for i in range(n):
        if sorted(arr[i]) != number:
            isYes = 0
            break
        if sorted(arr_reverse[i]) != number:
            isYes = 0
            break

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            tmp = []
            for k in range(3):
                tmp += arr[i+k][j:j+3]
            if sorted(tmp) != number:
                isYes = 0
                break
        if isYes == 0:
            break

    if isYes:
        print("YES")
    else:
        print("NO")