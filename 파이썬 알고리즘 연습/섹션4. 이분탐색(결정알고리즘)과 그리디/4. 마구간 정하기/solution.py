import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    n, c = map(int, input().split())
    arr = [int(input()) for _ in range(n)]
    arr.sort()
    # 마구간 최소와 최대의 중간을 구하고 중간과의 거리를 max거리로 놓는다
    # 그리고 그 거리만큼 주어진 개수가 들어가는지 확인한다.
    # 안되면 거리 반으로 줄인 후 개수가 들어가는지 확인한다.
    # 된다면 거기서부터 +1 시키면서 들어가는지 확인한다.
    # 안되는 순간이 오면 그 때의 거리 -1이 최대 거리이다.
    min_num = min(arr)
    max_num = max(arr)
    mid = (min_num + max_num) // (c-1)
    cnt = 1
    answer = 0
    while True:
        min_num = min(arr)
        max_num = max(arr)
        for i in range(1, n):
            if arr[i]-min_num > mid:
                cnt += 1
                min_num = arr[i]
                if cnt == c:
                    break
        if cnt == c:
            mid += 1
        if cnt < c:
            answer = mid - 1
            break
    print(answer)