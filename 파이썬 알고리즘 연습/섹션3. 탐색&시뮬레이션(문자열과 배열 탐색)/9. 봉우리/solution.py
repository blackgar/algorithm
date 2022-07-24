import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    answer = 0

    for y in range(n):
        for x in range(n):
            cnt = 0
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < n and 0 <= ny < n and arr[y][x] <= arr[ny][nx]:
                    cnt += 1
                if cnt > 0:
                    break
            if cnt == 0:
                answer += 1
    print(answer)

