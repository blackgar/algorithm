import sys

sys.stdin = open("input.txt")

def dfs(x, s):
    global cnt
    if x == m:
        cnt += 1
        for i in res:
            print(i, end=" ")
        print()
    else:
        for i in range(s, n+1):
            res[x] = i
            dfs(x+1, i+1)

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    res = [0] * m
    cnt = 0
    dfs(0, 1)
    print(cnt)

# def DFS(L, s):
#     global cnt
#     if L == m:
#         for j in range(L):
#             print(res[j], end=' ')
#         cnt += 1
#         print()
#     else:
#         for i in range(s, n+1):
#             res[L]=i
#             DFS(L+1, i+1)
#
# for tc in range(1, T + 1):
#     n, m = map(int, input().split())
#     res = [0] * (n+1)
#     cnt = 0
#     DFS(0, 1)

