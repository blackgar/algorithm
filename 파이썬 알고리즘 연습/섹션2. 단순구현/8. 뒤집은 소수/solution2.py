import sys

sys.stdin = open("input.txt")

# 문자열 숫자를 받아서 뒤집어 주는 함수
def reverse(x):
    return x[::-1]

# 문자열 숫자를 받아서 뒤집은 다음 0으로 시작되는 숫자를 제거해주는 함수
def delete_zero(x):
    tmp = reverse(x)
    # 뒤집은 수의 첫번째 자리가 0이면 다음 자리수를 검사하면서 연속된 0을 체크하고 연속된 0이 끝나면 그 부분까지 반환하는 함수
    for i in range(len(tmp)):
        if tmp[i] == "0":
            continue
        else:
            return int(tmp[i:])

# 문자열을 받아서 뒤집은 수의 연속된 0을 제거한 숫자를 받아서 소수인지 체크해주는 함수
def isPrime(x):
    number = delete_zero(x)
    # 1인 경우엔 소수가 아니므로 바로 False 반환
    if number == 1:
        return False
    # 소수일 경우 해당 숫자를 반환하고 소수가 아니면 False를 반환하도록
    for i in range(2, number):
        if number % i == 0:
            return False
    return number

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    arr = list(input().split())
    answer = []

    # 뒤집어서 연속된 0을 제거하고 소수인지를 체크하는 함수를 이용해서 체크한 후
    # 반환되는 값이 있다면 정답에 주가하고 반환되는게 False라면 정답 배열에 추가해서 출력하도록 구현.
    for num in arr:
        tmp = isPrime(num)
        if tmp:
            answer.append(tmp)

    print(*answer)