import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    result = []
    # 두 주사위를 던져서 나오는 모든 눈의 합 구하기
    for i in range(1, n+1):
        for j in range(1, m+1):
            result.append(i+j)
    # 해당 눈의 합에 해당하는 인덱스에 +1로 카운트 해주기
    arr = [0] * (len(result) + 1)
    for i in range(len(result)):
        arr[result[i]] += 1
    # 거기서 최대 값인 arr의 index가 결국 가장 높은 확률로 나올 수 있는 수이므로 그 수가 있다면 오름차순으로 list에 넣어서 출력해준다.
    tmp = max(arr)
    res = []
    for i in range(len(arr)):
        if arr[i] == tmp:
            res.append(i)
    # 리스트를 공백하나 사이로 띄워서 출력하기.
    print(*res)
    # result.sort()
    # tmp = result[0]
    # cnt = 1
    # res = [tmp, cnt]
    # for i in range(len(result)):
    #     if result[i] != tmp:
    #         tmp = result[i]
    #         cnt = 1
    #     else:
    #         cnt += 1