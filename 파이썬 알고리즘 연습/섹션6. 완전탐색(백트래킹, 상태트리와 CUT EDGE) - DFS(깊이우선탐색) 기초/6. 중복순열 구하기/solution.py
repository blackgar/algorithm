import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline
# s = input().rstrip()
def dfs(x):
    global cnt
    # 필요한 조합 다 찾은경우
    if x == m:
        # 순열 개수 더해주고 반복문 돌면서 res의 값 하나하나 뽑아오기
        cnt += 1
        for i in range(m):
            print(res[i], end=" ")
        print()
        return
    else:
        # 중복순열이기 때문에 자기 숫자를 포함한 n개 만큼 수를 조합해야 한다.
        # res라는 빈 리스트에 조합 숫자를 넣어서 순열을 만들고
        # depth를 들어간다.
        for i in range(1, n+1):
            res[x] = i
            dfs(x+1)

T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [i for i in range(1, n+1)]
    res = [0] * m
    cnt = 0
    # 순열 찾아주고
    dfs(0)
    # 총 개수 출력
    print(cnt)