import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    l = int(input())
    arr = list(map(int, input().split()))
    m = int(input())

    # min, max 사용
    for i in range(m):
        arr[arr.index(max(arr))] -= 1
        arr[arr.index(min(arr))] += 1

    print(max(arr) - min(arr))

    # min, max 사용x
    for i in range(m):
        arr.sort()
        arr[-1] -= 1
        arr[0] += 1
    arr.sort()
    print(arr[-1] - arr[0])