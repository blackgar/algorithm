import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    mid = n // 2
    answer = 0
    # 중간값을 기준으로해서 양쪽 한칸씩 늘려주는 방법으로 계산 진행
    # 밑으로 내려갈수록 중간 지점까지 증가하는 격자판 값들을 계산.
    for i in range(mid+1):
        answer += sum(arr[i][mid-i:mid+i+1])
    # 줄어드는 지점부터 마지막 줄까지의 격자판 값들을 계산
    for i in range(mid-1, -1, -1):
        answer += sum(arr[n-i-1][mid-i:mid+i+1])

    print(answer)