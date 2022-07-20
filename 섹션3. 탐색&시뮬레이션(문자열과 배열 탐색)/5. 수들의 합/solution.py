import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    # m이 되는 구간 회수 카운트
    cnt = 0
    # i번째 값을 기준으로 뒤에 수들을 더해나가면서 m이 되는 조건에서 cnt += 1

    for i in range(n):
        hap = arr[i]
        if hap == m:
            cnt += 1
            continue
        for j in range(i+1, n):
            hap += arr[j]
            if hap == m:
                cnt += 1
                break
            # 빠른 연산을 위해 hap이 m을 넘어가게 되면 break해서 다음 조건 찾으러 출발(가지치기)
            elif hap > m:
                break
    print(cnt)