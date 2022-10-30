import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    avg = round(sum(arr) / n)
    gap = 100
    closest_score = 0
    answer = 0

    # 차이를 비교해서 차이가 가장 적어야 하고
    # 만약 평균보다 큰 값이 차이가 가장 작다면 가장 먼저 발견되는 값이 정답이 되고
    # 평균보다 작은 값이 차이가 가장 작다면 가장 늦게 발견되는 값이 정답이 되어야 한다.
    for i in range(n):
        # 평균과의 차이를 절대값으로 계산하고
        tmp = abs(arr[i]-avg)
        # 만약 현재 차이가 기존 차이보다 작으면 차이 값을 갱신해주면서 정답은 현재 학생의 점수이므로 위치를 answer에 저장
        # 그리고 차이가 같을 때 더 높은 점수인 경우를 출력해야 하므로 closest_score이라는 변수에 현재 점수를 저장해준다.
        if tmp < gap:
            gap = tmp
            answer = i+1
            closest_score = arr[i]
        # 만약 기존의 차이와 현재 차이가 같다면
        elif tmp == gap:
            # 지금 점수가 기존에 있던 점수보다 크면 정답 학생의 위치를 answer에 갱신시켜 준다.
            # 이렇게 되면 추후에 같은 점수를 발견하더라도 가장 먼저 발견된 학생의 위치를 기억할 수 있게 된다.
            if closest_score < arr[i]:
                answer = i+1
    print(avg, answer)
