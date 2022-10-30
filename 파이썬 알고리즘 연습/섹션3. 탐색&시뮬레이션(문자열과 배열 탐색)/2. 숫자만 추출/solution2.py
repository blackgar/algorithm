import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    word = input()
    number = ""
    cnt = 0
    # 숫자만 추출하기 위해서 isdigit()메서드로 숫자인 부분만 number 변수에 추가
    for letter in word:
        if letter.isdigit():
            number += letter
    # 첫 자리가 0이면서 연속된 0이 나오게 되면 그 부분을 제거하고 남은 부분만 정수로 변환
    for i in range(len(number)):
        if number[i] == "0":
            continue
        else:
            number = int(number[i:])
            break
    # 1부터 나눠 떨어지면 약수로 개수를 카운트 해준다.
    for i in range(1, number+1):
        if number % i == 0:
            cnt += 1
    print(number)
    print(cnt)

