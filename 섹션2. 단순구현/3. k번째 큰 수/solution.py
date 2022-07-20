import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    n, K = map(int, input().split())
    numbers = list(map(int, input().split()))
    # 3장의 카드를 합한 값 모두 기록
    result = []
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                tmp = numbers[i] + numbers[j] + numbers[k]
                result.append(tmp)
    # 그 중에서 중복되는 것들 set로 제거해서 다시 list화(index 활용을 위해)
    res = list(set(sorted(result)))
    # 정렬한 후 정렬 된 res안에서 뒤에서 K를 뺀 위치의 숫자가 K번째로 큰 수
    res.sort()
    # print(res)
    # print(n, K)
    print(res[len(res)-K])


