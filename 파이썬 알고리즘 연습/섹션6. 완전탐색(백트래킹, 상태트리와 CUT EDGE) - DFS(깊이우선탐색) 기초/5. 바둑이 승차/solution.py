import sys

sys.stdin = open("input.txt")

def dfs(i, sum, tsum):
    global max_truck
    # 지금까지 조합을 만든 수에 남은 가지의 모든 값들을 더해도 최대값보다 작으면 더 탐색할 필요 없으므로
    # 여기서 가지치기 해준다.
    # tsum(지금까지 거쳐온 가지들의 총합)을 total에서 빼주면 남아있는 가지들의 총합
    if sum + (total-tsum) < max_truck:
        return
    # 끝까지 탐색하거나 바둑이들의 무게가 조건을 넘어갈 경우 더 탐색이 필요 없으므로 조건분기 해준다
    if i >= n or sum > c:
        # 이때 sum값이 조건보다 작고 지금까지 발견된 최대값보다 크다면 최대값 갱신
        if sum <= c and sum > max_truck:
            max_truck = sum
            return
        return
    else:
        dfs(i+1, sum + arr[i], tsum + arr[i])
        dfs(i+1, sum, tsum + arr[i])

T = int(input())

for tc in range(1, T + 1):
    c, n = map(int, input().split())
    arr = [int(input()) for _ in range(n)]
    total = sum(arr)
    max_truck = 0
    dfs(0, 0, 0)

    print(max_truck)