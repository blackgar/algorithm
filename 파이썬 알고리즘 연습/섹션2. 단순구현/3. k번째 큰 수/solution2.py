import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    result = []
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                hap = arr[i]+arr[j]+arr[k]
                if hap in result:
                    continue
                result.append(hap)
    result.sort()
    answer = result[len(result)-K]
    print(answer)