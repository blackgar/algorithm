import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # 1
    # arr_reverse라는 arr의 세로줄만 모아줄 배열 선언
    arr_reverse = []
    result = []
    # zip함수를 이용해서 세로줄을 arr_reverse에 삽입
    for i in zip(*arr):
        arr_reverse.append(i)
    # 왼쪽/오른쪽 대각선 합 변수
    hap_crossL = 0
    hap_crossR = 0
    # 한번의 for문으로 sum함수로 가로줄, 세로줄 합을 구해서 result에 담는다
    for i in range(n):
        result.append(sum(arr[i][:]))
        result.append(sum(arr_reverse[i][:]))
        # 가로 세로 대각선 합을 구한다
        hap_crossL += arr[i][i]
        hap_crossR += arr[i][n-i-1]
    result.append(hap_crossR)
    result.append(hap_crossL)
    # 제일 큰 수 출력한다.
    print(max(result))

    # 2
    # 위와 방법은 같으나 max_num이라는 변수로 비교를 통한 최대값 출력
    arr_reverse = []
    result = []
    for i in zip(*arr):
        arr_reverse.append(i)
    hap_crossL = 0
    hap_crossR = 0
    max_num = 0
    for i in range(n):
        hap_vertical = sum(arr[i][:])
        hap_horizontal = sum(arr_reverse[i][:])
        hap_crossL += arr[i][i]
        hap_crossR += arr[i][n-i-1]
        if max_num >= hap_horizontal and max_num >= hap_vertical:
            continue
        else:
            max_num = max(hap_horizontal, hap_vertical)
    if max_num < hap_crossL or max_num < hap_crossR:
        max_num = max(hap_crossR, hap_crossL)
    print(max_num)

    # 3
    # sumation 함수 없이 index로 각 값들을 계산한 후 최대 값 출력하기.
    result = []
    hap_crossL = 0
    hap_crossR = 0

    for i in range(n):
        hap_vertical = 0
        hap_horizontal = 0
        hap_crossL += arr[i][i]
        hap_crossR += arr[i][n-i-1]
        for j in range(n):
            hap_vertical += arr[i][j]
            hap_horizontal += arr[j][i]
        result.append(hap_vertical)
        result.append(hap_horizontal)
    result.append(hap_crossR)
    result.append(hap_crossL)

    print(max(result))


