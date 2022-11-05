import sys
import heapq as hq

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    print(tc, "번째 test")
    a = []
    while True:
        n = int(input())
        if n == -1:
            break
        if n == 0:
            if len(a) == 0:
                print(-1)
            else:
                print(hq.heappop(a))
        else:
            hq.heappush(a, n)
    # print(a)