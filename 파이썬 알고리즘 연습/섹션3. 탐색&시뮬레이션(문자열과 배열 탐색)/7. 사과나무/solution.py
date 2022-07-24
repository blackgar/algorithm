import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    hap = 0
    for i in range(n//2+1):
        hap += sum(arr[i][n//2-i:n//2+i+1])
    for i in range(n-1, n//2, -1):
        hap += sum(arr[i][n//2-n+1+i:n//2+n-i])

    print(hap)