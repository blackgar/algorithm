import sys

sys.stdin = open("input.txt")

def dfs(x):
    if x > n:
        for i in range(1, n+1):
            if visited[i]:
                print(i, end=" ")
        print()
        return
    else:
        visited[x] = 1
        dfs(x+1)
        visited[x] = 0
        dfs(x+1)




T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    visited = [0] * (n+1)
    dfs(1)