import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    # 에라토스테네스의 체
    # 만약 2가 소수라면 2의 배수는 모두 소수가 아니다.
    # 만약 3이 소수라면 3의 배수는 모두 소수가 아니다.
    # 이런 논리로 배열에 0, 1은 소수가 아니므로 False로 두고
    # 나머지 숫자에 True로 넣은 후 배열을 돌면서 만약 그 숫자가
    # 소수라면 그 배수를 모두 False로 바꿔주면서 배열안에 남아있는
    # True의 개수가 곧 소수의 개수이므로 관련된 내용 출력하기
    arr = [False, False] + [True] * (n-1)

    for i in range(2, n):
        if arr[i]:
            for j in range(2*i, n+1, i):
                arr[j] = False
    print(arr.count(True))