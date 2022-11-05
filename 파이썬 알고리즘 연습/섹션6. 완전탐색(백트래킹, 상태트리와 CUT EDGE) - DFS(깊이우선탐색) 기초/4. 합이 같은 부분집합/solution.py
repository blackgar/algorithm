import sys

sys.stdin = open("input.txt")

# 처음 접근방식
def dfs(x, i):
    global answer
    index = i + 1
    if index > n:
        hap = 0
        for v in range(1, max(arr)+1):
            if visited[v]:
                hap += v
        if hap == total-hap:
            answer = "YES"
            return
        return
    else:
        if index >= n:
            visited[x] = 1
            dfs(arr[index - 1], index)
            visited[x] = 0
            dfs(arr[index - 1], index)
        else:
            visited[x] = 1
            dfs(arr[index], index)
            visited[x] = 0
            dfs(arr[index], index)
# 리팩토링
def dfs2(i, sum):
    global answer2
    # 절반을 넘어가면 나머지 부분집합을 합해도 절반이 안되므로 더 확인할 필요가 없어지므로 return
    # 효율성 체크
    if sum > total // 2:
        return
    # 끝까지 조합을 더해서 그게 나머지 값과 같아야 합이 같은 부분집합이다.
    if i == n:
        if sum == total-sum:
            answer2 = "YES"
            return
    else:
        # 그 값을 더하고
        dfs2(i+1, sum+arr[i])
        # 그 값을 더하지 않고
        dfs2(i+1, sum)

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    total = sum(arr)
    visited = [0] * (max(arr)+1)
    answer = "NO"
    answer2 = "NO"

    dfs(arr[0], 0)
    dfs2(0, 0)

    print(answer)
    print(answer2)