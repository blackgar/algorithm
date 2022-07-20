import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = 0

    # 일단 배열로 받아온 사람들이 뽑은 주사위 기록들을 반복하면서
    # 각 기록별 수들을 비교해서 3개가 같은지 2개가 같은지 다 다른지 체크 하는 반복문과
    # 각 상황별 상금을 계산한 다음 result라는 변수에 담긴 상금보다 크면 result를 갱신해주면서
    # 마지막에 담겨있는 최대 상금인 result를 출력한다.
    for i in range(n):
        for j in arr[i]:
            first_prize = 10000 + j * 1000
            second_prize = 1000 + j * 100
            third_prize = max(arr[i]) * 100
            if arr[i].count(j) == 3 and first_prize > result:
                result = first_prize
                break
            elif arr[i].count(j) == 2 and second_prize > result:
                result = second_prize
                break
            if arr[i][0] != arr[i][1] != arr[i][2] and third_prize > result:
                result = third_prize
                break
    print(result)