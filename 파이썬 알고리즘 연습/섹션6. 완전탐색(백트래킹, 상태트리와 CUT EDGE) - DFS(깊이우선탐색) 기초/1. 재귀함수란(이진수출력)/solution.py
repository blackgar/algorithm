import sys

sys.stdin = open("input.txt")

def make_bin(x):
    global answer
    if x == 0:
        return
    else:
        make_bin(x // 2)
        answer += str(x % 2)
    # 23 => make_bin(11) => make_bin(5) => make_bin(2) => make_bin(1) => make_bin(0) return
    # make_bin(1), answer += 1 => make_bin(2), answer += 0 => make_bin(5), answer += 1 =>
    # make_bin(11), answer += 1 => make_bin(23), answer += 1
    # => answer = 10111

if __name__=="__main__":
    T = int(input())
    for tc in range(1, T + 1):
        print(tc, "번째 test")
        n = int(input())
        answer = ""
        make_bin(n)
        print(answer)