import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    result = [1] * (n+1)
    # 처음에 발견된 소수의 배수는 소수가 아니다를 이용해서 접근하기
    for i in range(2, n):
        if result[i]:
            for j in range(i*2, n+1, i):
                result[j] = 0

    print(result.count(1)-2)