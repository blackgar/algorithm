import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    K, n = map(int, input().split())
    arr = [int(input()) for _ in range(K)]
    mid_length = max(arr) // 2
    flag = False
    answer = 0
    # 랜선 길이는 arr의 최대값에서 출발해서 반씩 잘라가면서 나아가면 된다.
    # 반으로 잘라서 배열 돌면서 그 길이만큼으로 나눠서 cnt가 필요한 개수보다 크면 다시 반으로 나눠서 찾고
    # 만약 거기서 반 나눴는데 cnt가 필요한 개수보다 작으면 다시 기존의 값과 현재 찾는 값 사이 값으로 찾는다.
    # 그러다가 딱 숫자가 맞는 구간이 나오게 되면 거기서부터 하나씩 크기를 더해가면서 조건을 만족하는 최대값을 찾는다.
    gap = 1
    start = max(arr)
    end = 0
    while True:
        cnt = 0
        # print(start, answer)
        for j in range(K):
            cnt += arr[j] // start
        if cnt >= n:
            flag = True
            answer = start
            start += 1
        else:
            if flag:
                break
            else:
                end = start
                start //= 2

    print(answer)
