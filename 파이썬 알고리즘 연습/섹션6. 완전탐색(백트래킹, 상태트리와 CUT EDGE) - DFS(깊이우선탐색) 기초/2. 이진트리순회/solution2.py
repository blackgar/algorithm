import sys

sys.stdin = open("input.txt")

def dfs(x, i):
    if x == 3:
        return
    else:
        # 전위 순회
        print(i, end=" ")
        dfs(x+1, i*2)
        # 중위 순회
        print(i, end=" ")
        dfs(x+1, i*2+1)
        # 후위 순회
        print(i, end=" ")

def dfs2(x):
    if x > 7:
        return
    else:
        print(x, end=" ")
        dfs2(x*2)
        dfs2(x*2+1)
# dfs(0, 1)
dfs2(1)