import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # 우하좌상으로 사방을 체크해주기 위한 방향 인덱스
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    answer = 0

    for y in range(n):
        for x in range(n):
            # 만약 현재 칸보다 큰 칸이 사방향 중에 있으면 False로 바꿔서 봉우리로 카운트 하기 위한 변수
            flag = True
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 상하좌우 사방향을 체크했을 때 그 곳이 격자판을 벗어나지 않은 상태에서 현재 칸보다
                # 큰 값이 발견되면 봉우리가 아니므로 False 입력
                if 0 <= nx < n and 0 <= ny < n and arr[ny][nx] >= arr[y][x]:
                    flag = False
                    break
            # 봉우리라면 카운트해주고 아니면 다시 다음 봉우리를 찾으러 이동
            if flag:
                answer += 1

    print(answer)
