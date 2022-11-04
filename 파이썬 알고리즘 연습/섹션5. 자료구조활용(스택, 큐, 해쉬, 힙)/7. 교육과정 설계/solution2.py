import sys
from collections import deque

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    mandatory = list(input())
    n = int(input())
    lecture_list = [input() for _ in range(n)]
    print(tc)
    # 1
    for i in lecture_list:
        answer = "NO"
        tmp = []
        for j in i:
            if j in mandatory and j not in tmp:
                tmp.append(j)
                if tmp[len(tmp)-1] != mandatory[len(tmp)-1]:
                    print("더 빠름")
                    break
                # print(tmp)
            if len(tmp) == len(mandatory):
                if tmp == mandatory:
                    answer = "YES"

    # 2 queue로 풀기
    for i in lecture_list:
        answer = "YES"
        need = deque(mandatory)
        for j in i:
            if j in need:
                if j != need.popleft():
                    answer = "NO"
                    break
        else:
            if len(need) > 0:
                answer = "NO"
        print(answer)