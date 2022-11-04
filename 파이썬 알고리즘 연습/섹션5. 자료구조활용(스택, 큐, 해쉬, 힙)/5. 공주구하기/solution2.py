import sys
from collections import deque
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    n, k = map(int, input().split())
    prince = [i for i in range(1, n+1)]
    # deque 활용하는 방법
    dq = deque(prince)
    cnt = 0
    while len(prince) > 1:
        cnt += 1
        if cnt % k == 0:
            # deque로 popleft 쓰거나
            # 그냥 배열에서 pop(index)로 처리할 수 있다.
            prince.pop(0)
            dq.popleft()
        else:
            dq.append(dq.popleft())
            prince.append(prince.pop(0))
    print(prince[0])
    print(dq[0])
