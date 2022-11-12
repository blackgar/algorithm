import sys

sys.stdin = open("input.txt")

# 2진수는 결국 2로 나눈 나머지 값을 남기고 다음 자리수로 이동하므로
# 11 => 몫 5 나머지 1 => 몫 2 나머지 1 => 몫 1 나머지 0 => 몫 0 나머지 1
# 이는 2진수의 첫째자리부터 계산한 것이므로 출력을 몫이 0이 됐을 때 부터 해야하므로
# 후위순회로 출력하면 된다.
def recur(x):
    if x == 0:
        return
    else:
        recur(x//2)
        print(x % 2, end="")

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    recur(n)
    print()