import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    answer = 0

    for i in range(n):
        hap = arr[i]
        if sum(arr[i:]) < m:
            break
        if hap >= m:
            if hap == m:
                answer += 1
            continue
        for j in range(i+1, n):
            hap += arr[j]
            if hap >= m:
                if hap == m:
                    answer += 1
                break

    print(answer)