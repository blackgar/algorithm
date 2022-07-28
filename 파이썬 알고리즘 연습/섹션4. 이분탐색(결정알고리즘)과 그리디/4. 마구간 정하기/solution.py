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
    distance = (max(arr)-min(arr)) // c
    cnt = 1
    answer = n
    while True:
        result = [arr[0]]
        min_num = min(arr)
        max_num = max(arr)
        for i in range(1, n):
            if arr[i]-min_num > distance:
                cnt += 1
                result.append(arr[i])
                min_num = arr[i]
                if cnt > c:
                    break
        if cnt == c:
            distance += 1
        elif cnt < c:
            distance // 2
        elif cnt > c:
            break

    for i in range(len(result)-1):
        if arr[i+1] - arr[i] < answer:
            answer = arr[i+1] - arr[i]

    print(answer)