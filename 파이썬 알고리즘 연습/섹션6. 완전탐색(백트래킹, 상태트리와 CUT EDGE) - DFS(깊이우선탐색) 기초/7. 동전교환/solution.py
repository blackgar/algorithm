import sys

sys.stdin = open("input.txt")

def dfs(x, hap):
    global cnt
    # 만약 현재 동전 조합의 합이 거스름돈을 넘어서면 안되고, 현재까지 발견된 최소 동전 숫자보다 카운트 되고 있는게
    # 즉 dfs레벨이 높다면 더 찾을 필요 없음.
    if hap > m or x >= cnt:
        return
    # 동전 조합의 합이 거스름돈과 일치하고 개수가 현재까지 발견된거보다 작다면 동전 수 갱신
    if hap == m and cnt > x:
        cnt = x
        return
    else:
        # 동전을 하나 선택하는걸로 dfs 레벨을 높이고 동전은 총 arr에 들어있는 동전을 선택하는 것으로 조합이 맞춰지므로
        # for문을 돌리면서 dfs로 조합찾아 나가기.
        for i in range(n):
            dfs(x+1, hap + arr[i])

# D(0) => x=0, hap=0 => arr[0]

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    # 동전 찾기는 큰 동전부터의 조합을 찾는게 시간이 적게 걸린다.
    arr.sort(reverse=True)
    cnt = 500
    # 반복문으로 풀기 => 3번 TC에서 문제 발생. 50 50 25 1*4 이렇게 되는데, 사실 50*2 20 8 1 하면 5개로 더 적음
    # for coin in arr[::-1]:
    #     # print(coin, m, cnt)
    #     if m:
    #         cnt += m // coin
    #         m %= coin
    #     else:
    #         break
    dfs(0, 0)
    print(cnt)
    # 재귀로 풀기
