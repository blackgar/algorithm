import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    word = input()
    number = []
    # 숫자만 찾기 위한 숫자 배열
    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    # 약수의 개수를 구해줄 변수
    cnt = 0
    # 일단 숫자들만 따로 찾아 number에 담아준다.
    for i in range(len(word)):
        if word[i] in numbers:
            number.append(word[i])
    # 0으로 시작하는 수들은 0을 제거해주기 위한 로직
    for i in range(len(number)):
        # 0이면 다음 0을 찾으러 가고
        if number[i] == 0:
            continue
        # 0이 아닌 수를 만나면 거기서 부터 끝까지의 수를 찾아서 number 갱신
        else:
            number = int(''.join(number[i:]))
            break
    # 약수를 찾기 위해 1부터 자기 자신까지 나눠서 떨어지는 수를 cnt에 더해준다.
    for i in range(1, number+1):
        if number % i == 0:
            cnt += 1
    print(number)
    print(cnt)