import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    answer = 0
    # 채점 결과 list를 받아와서 연속으로 맞춘 개수를 cnt로 세어주고
    # 그 개수 만큼을 점수로 answer에 더해줌으로써 연속된 문제의 정답은 가산해서 계산이 되고 틀린 경우 0으로 초기화되어
    # 다시 1부터 계산될 수 있도록 구현
    for i in arr:
        if i == 1:
            cnt += 1
            answer += cnt
        else:
            cnt = 0
    print(answer)