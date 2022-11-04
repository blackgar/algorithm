import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    ana = dict()
    answer = "YES"
    for i in input():
        # dictionary에서 key가 없을 때는 생성해주고 있을 때는 그 키에 해당하는 값에 접근할 수 있게 해주는 함수 get
        ana[i] = ana.get(i, 0) + 1
        # 위 함수와 아래 조건문이 같은 동작을 한다.
        if i in ana.keys():
            ana[i] += 1
        else:
            ana[i] = 1
    print(ana)
    for j in input():
        ana[j] -= 1
        # 위 코드와 동일한 방법
        ana[j] = ana.get(j, 0) - 1
    print(ana)
    for key, val in ana.items():
        if val != 0:
            answer = "NO"
            break
    print(answer)
