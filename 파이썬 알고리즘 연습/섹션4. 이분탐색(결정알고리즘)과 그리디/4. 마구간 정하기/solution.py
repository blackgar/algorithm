import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    n, c = map(int, input().split())
    arr = [int(input()) for _ in range(n)]
    arr.sort()
