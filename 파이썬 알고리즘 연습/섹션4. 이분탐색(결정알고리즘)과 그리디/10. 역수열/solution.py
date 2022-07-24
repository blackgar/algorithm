import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    # 1=>5 2=>3
    # 3=>5여야 하는데 이미 1이 있어서 다음인 6
    # 4=>0
    # 5=>3이어야하는데 이미 2가 그 자리에 있으므로 4
    # 6=>2 7=>7 8=>1



