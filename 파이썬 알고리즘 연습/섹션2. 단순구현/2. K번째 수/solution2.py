import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    n, s, e, k = map(int, input().split())

    # 내장 Method로 푸는 방법
    # arr = sorted(list(map(int, input().split()))[s-1:e])

    # Bubble Sort로 푸는 방법
    arr = list(map(int, input().split()))
    arr = arr[s-1:e]
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    print(arr[k-1])
