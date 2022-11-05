import sys

sys.stdin = open("input.txt")

def dfs(x):
    global answer
    if answer:
        return
    if x == n:
        tmp = 0
        for i in range(n):
            tmp += compare[i] * int(res[i])
        if tmp == f:
            answer = " ".join(res)
        return
    else:
        for i in range(1, n+1):
            if not visited[i]:
                visited[i] = 1
                res[x] = str(i)
                dfs(x+1)
                visited[i] = 0
def dfs2(x, hap):
    global answer
    if answer:
        return
    if x == n and hap == f:
        tmp = ""
        for num in res:
            tmp += str(num) + " "
        answer = tmp
        return
    else:
        for i in range(1, n+1):
            if not visited[i]:
                visited[i] = 1
                res[x] = i
                dfs2(x+1, hap + (compare[x]*res[x]))
                visited[i] = 0

# 16이면 두갈래 뻗어서 16이 되는 조합찾기
# 그 조합을 만족하는 각 조합 숫자에서 또 하나씩 두갈래로 뻗어나가서 조합찾기
# 그렇게 조합을 다 찾으면 그 최종 노드값들 출력

T = int(input())

for tc in range(1, T + 1):
    n, f = map(int, input().split())
    res = [0] * n
    compare = [1] * n
    visited = [0] * (n+1)
    answer = ""
    for i in range(1, n):
        compare[i] = compare[i-1] * (n-i) // i
    # print(compare)
    # dfs(0)
    dfs2(0, 0)
    print(answer)