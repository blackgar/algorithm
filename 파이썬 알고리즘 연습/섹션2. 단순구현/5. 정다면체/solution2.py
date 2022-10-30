import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    # 나올 수 있는 눈의 합을 인덱스에 맞게 숫자를 세어주기 위한 배열
    result = [0]*(n+m+1)
    answer = []
    # 반복문을 돌면서 나올 수 있는 눈의 합에 맞는 인덱스에 값을 1씩 더해준다.
    for i in range(1, n+1):
        for j in range(1, m+1):
            result[i+j] += 1
    # 제일 많이 나온 합의 개수를 구하고
    highest_hap = max(result)
    # 반복문을 돌면서 제일 많이 나온 합의 개수를 가진 합을 정답 배열에 추가한다.
    for i in range(len(result)):
        if result[i] == highest_hap:
            answer.append(i)
    print(*answer)
