import sys

sys.stdin = open("input.txt")

# 문자열 숫자가 들어오면 정수로 변환해서 각 자릿수를 계산해주는 함수
def digit_sum(x):
    hap = 0
    for i in x:
        hap += int(i)
    return hap

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    arr = list(input().split())
    max_num = 0
    answer = ""
    # 반복문을 돌면서 자릿수를 계산했을 때 그 값이 현재 자릿수 최대값보다 크면 값을 갱신해주고 정답을 현재 문자열 숫자로 갱신
    for num in arr:
        if max_num < digit_sum(num):
            max_num = digit_sum(num)
            answer = num
    print(answer)