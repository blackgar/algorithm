import sys

sys.stdin = open("input.txt")

# 1 2 3
def dfs(x):
    if x > n:
        for i in range(1, n+1):
            if visited[i]:
                print(i, end=" ")
        print()
        return
    else:
        # 해당 숫자 x를 선택하고 다음 숫자를 선택하러 간다.
        visited[x] = 1
        dfs(x+1)
        # 해당 숫자를 선택하지 않고 다음 숫자를 선택하러 간다.
        visited[x] = 0
        dfs(x+1)

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    visited = [0] * (n+1)
    dfs(1)