import sys

sys.stdin = open("in3.txt")

T = int(input())

for tc in range(1, T + 1):
    n, s, e, k = map(int, input().split())
    arr = list(map(int, input().split()))
    # 구간 나누고
    numbers = arr[s-1:e]
    # 해당 구간 sort해서 k번째 수 찾기
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            tmp = numbers[i]
            if tmp > numbers[j]:
                numbers[i] = numbers[j]
                numbers[j] = tmp
    print(numbers[k-1])