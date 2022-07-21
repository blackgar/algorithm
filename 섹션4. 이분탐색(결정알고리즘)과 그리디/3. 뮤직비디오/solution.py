import sys
import math

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    avg = math.ceil(sum(arr) / m)

    # 일단 평균부터 시작을 해서 하나씩 키워나가본다.
    # dvd 하나에 범위 안으로 노래들을 넣고 범위를 초과하면 다음 dvd에 넣는다.
    # 정해진 dvd 개수안에 노래가 다 안들어갈 경우엔 범위를 1씩 늘려주면서 담기는 순간까지 계산한다.
    # 마지막에 남은 범위보다 지금 현재 가지고 있는 범위가 작다면 전부 다 넣을 수 있다는 것이므로 그렇게 처리하고 break하고 answer정해주기

    loc = 0
    total = 0
    flag = False
    while True:
        dvd = [0] * m
        # print("Let's Go")
        for i in range(n):
            # print(dvd)
            # print("Location", loc)
            # print("Average", avg)
            if arr[i] > avg or loc >= m:
                break
            if dvd[loc] + arr[i] <= avg:
                dvd[loc] += arr[i]
                total += arr[i]
            else:
                loc += 1
                if loc == m:
                    break
                dvd[loc] += arr[i]
                total += arr[i]
            if total == sum(arr):
                flag = True

        if flag:
            break
        else:
            avg += 1
            loc = 0
            total = 0
    print(avg)