import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    n = 10
    arr = [i for i in range(1, 21)]

    # 총 10줄의 구간이 주어지므로 10번의 반복문 동안 해당 구간을 해당 구간을 뒤집은 값으로 바꿔주면 된다.
    for i in range(n):
        a, b = map(int, input().split())
        arr[a-1:b] = arr[a-1:b][::-1]

    print(arr)
