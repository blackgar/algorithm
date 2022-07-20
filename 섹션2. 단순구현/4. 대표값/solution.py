import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    numbers = list(map(int, input().split()))
    # round 함수를 통해 평균 반올림 진행
    avg = round(sum(numbers)/n)
    # 가장 평균에 가까운 수를 찾기 위해 gap을 계산
    # gap을 계산할 때는 절대값으로 차이를 계산해주고
    # 그 차이가 가장 작은 곳의 index + 1이 그 학생번호
    gap = []
    for i in range(n):
        gap.append(abs(numbers[i] - avg))
    # print(gap)
    print(avg, gap.index(min(gap))+1)


