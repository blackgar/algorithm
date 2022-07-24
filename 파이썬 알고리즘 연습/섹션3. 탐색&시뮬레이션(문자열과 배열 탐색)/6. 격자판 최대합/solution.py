import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # 세로 줄을 담아줄 배열
    arr_reverse = []
    result = []
    # 세로 줄을 담아주는 방법 zip함수를 통해 세로 줄을 한 줄씩 받아서 새로운 배열에 넣어준다.
    for i in zip(*arr):
        arr_reverse.append(list(i))
    # 왼쪽 대각선 합 담아줄 변수
    cross_1 = 0
    # 오른쪽 대각선 합 담아줄 변수
    cross_2 = 0
    for i in range(n):
        # 가로 한줄 합
        result.append(sum(arr[i][:]))
        # 세로 한줄 합
        result.append(sum(arr_reverse[i][:]))
        # 왼쪽 대각선 하나씩 담기
        cross_1 += arr[i][i]
        # 오른쪽 대각선 하나씩 담기
        cross_2 += arr[i][-i-1]
    # 대각선 값들 result에 담아주기
    result.append(cross_1)
    result.append(cross_2)
    # 합 중 가장 큰 값 출력하기.
    # 메서드 사용이 안된다면 오름차순 정렬해서 가장 끝 값 가져오기
    print(max(result))