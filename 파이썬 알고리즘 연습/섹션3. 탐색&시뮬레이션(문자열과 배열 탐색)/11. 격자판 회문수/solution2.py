import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(7)]
    arr_reverse = []
    answer = 0

    for i in zip(*arr):
        arr_reverse.append(i)

    for i in range(7):
        for j in range(3):
            if arr[i][j:j+5] == arr[i][j:j+5][::-1] or arr_reverse[i][j:j+5] == arr_reverse[i][j:j+5][::-1]:
                answer += 1

    print(answer)