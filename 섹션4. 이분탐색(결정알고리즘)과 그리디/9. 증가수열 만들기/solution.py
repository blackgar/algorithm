import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    tmp = 0
    answer = ''

    while True:
        if (arr[0] < tmp and arr[-1] < tmp) or len(arr) == 0:
            break
        if arr[0] > tmp and arr[-1] < tmp:
            tmp = arr[0]
            arr = arr[1:]
            answer += "L"
        elif arr[-1] > tmp and arr[0] < tmp:
            tmp = arr[-1]
            arr = arr[:-1]
            answer += "R"
        elif arr[0] > tmp and arr[0] < arr[-1]:
            tmp = arr[0]
            arr = arr[1:]
            answer += "L"
        elif arr[-1] > tmp and arr[0] > arr[-1]:
            tmp = arr[-1]
            arr = arr[:-1]
            answer += "R"

    print(len(answer))
    print(answer)