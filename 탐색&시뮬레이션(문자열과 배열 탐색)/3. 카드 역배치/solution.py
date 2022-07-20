import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    # 총 10개의 줄이 주어진다
    n = 10
    # 각 구간을 받아준다
    arr = [list(map(int, input().split())) for _ in range(n)]
    # 1, 20까지의 배열을 만들어준다.
    numbers = [i for i in range(1, 20+1)]

    # 반복문을 돌면서 위치를 바꿔준다.
    for i in range(n):
        # 기준이 되는 구간을 tmp라는 변수에 저장해주고
        tmp = numbers[arr[i][0]-1:arr[i][1]]
        # 해당 구간에 tmp를 뒤집은 배열을 넣어준다.(뒤집기)
        numbers[arr[i][0]-1:arr[i][1]] = tmp[::-1]
    # 구간별 뒤집기를 마친 후 배열을 출력해준다.
    print(*numbers)