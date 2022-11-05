import sys

sys.stdin = open("input.txt")

# 방문처리 대신 조건문 처리로 푼 방법
def dfs(x):
    global cnt
    # 2가지 조합 찾았으면
    if x == m:
        # res 값 중 중복된게 있으면 안되므로 체크해서 없으면 tmp에 담아서 출력
        tmp = ""
        for i in range(m):
            if res.count(res[i]) > 1:
                return
            else:
                tmp += str(res[i]) + " "
        cnt += 1
        print(tmp)
        return
    else:
        # 중복 순열까지 모두 찾는다. 위에 if 조건문에서 조건을 만족하는 값들을 출력하고 cnt에 더해준다.
        for i in range(1, n+1):
            res[x] = i
            dfs(x+1)
# 방문 처리를 통해 푸는 방법
def dfs2(x):
    global cnt2
    # 2가지 찾았으면 값을 그냥 출력해준다.
    if x == m:
        cnt2 += 1
        for i in range(m):
            print(res2[i], end=" ")
        print()
        return
    else:
        for i in range(1, n+1):
            # 만약 그곳을 방문하지 않았다면 dfs 한층 더 진행
            if not visited[i]:
                # 방문처리 해주고 res에 조합 하나 넣고 다음 숫자 찾는다.
                visited[i] = 1
                res2[x] = i
                dfs2(x+1)
                # 숫자 찾고 나왔으면 방문처리를 풀어줘야 나왔다는 것을 알 수 있다.
                visited[i] = 0


T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    res = [0] * m
    cnt = 0
    dfs(0)
    visited = [0] * (n + 1)
    res2 = [0] * m
    cnt2 = 0
    dfs2(0)
    print(cnt)
    print(cnt2)