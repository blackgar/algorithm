import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    arr = [input() for _ in range(n)]
    for i in range(len(arr)):
        # 대소문자를 구분하지 않는다는 부분을 구현하기 위해 lower메소드로 소문자로 다 변경한 후 비교
        if arr[i].lower() == arr[i][::-1].lower():
            print('#{} {}'.format(i+1, "YES"))
        else:
            print('#{} {}'.format(i+1, "NO"))