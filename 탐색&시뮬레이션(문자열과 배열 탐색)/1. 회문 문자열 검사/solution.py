import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    # 대소문자를 구분하지 않아야 하므로 소문자나 대문자로 다 바꿔준 후 회문 검사
    arr = [input().lower() for _ in range(n)]

    for i in range(n):
        # 리스트 슬라이싱 활용해 회문 검사
        if arr[i] == arr[i][::-1]:
            print("YES")
        else:
            print("NO")