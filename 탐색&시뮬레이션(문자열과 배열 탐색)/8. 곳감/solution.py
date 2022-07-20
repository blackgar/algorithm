import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    m = int(input())
    rotate = [list(map(int, input().split())) for _ in range(m)]
    hap = 0
    for i in range(m):
        tmp = arr[rotate[i][0] - 1][:]
        if rotate[i][1] == 0:
            for j in range(n):
                if j+rotate[i][2] > n:
                    arr[rotate[i][0]-1][j] = tmp[(j+rotate[i][2]) % n]
                else:
                    arr[rotate[i][0]-1][j] = tmp[(j+rotate[i][2]) % n]
        else:
            for j in range(n):
                arr[rotate[i][0] - 1][j] = tmp[j-rotate[i][2]]
    for i in range(n//2 + 1):
        hap += sum(arr[n//2-i][n//2-i:n//2+i+1])

    for i in range(n//2+1, n): # 4 5 6
        hap += sum(arr[i][n//2-(i-n//2):n//2+(i-n//2)+1])
    print(hap)