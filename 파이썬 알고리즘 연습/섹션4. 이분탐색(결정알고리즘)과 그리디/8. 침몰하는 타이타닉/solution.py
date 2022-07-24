import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    cnt = 0

    while True:
        # print(arr, cnt)
        if len(arr) == 0:
            break
        elif len(arr) < 2:
            cnt += 1
            break
        tmp = 0
        for i in range(1, len(arr)):
            if arr[0] + arr[i] <= m:
                tmp = arr[i]
                break
        if tmp != 0:
            arr.remove(tmp)
        arr.remove(arr[0])
        cnt += 1
    print(cnt)