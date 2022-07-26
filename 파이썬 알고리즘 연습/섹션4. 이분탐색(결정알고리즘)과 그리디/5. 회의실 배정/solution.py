import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr.sort()
    # 시작시간이 동일하지만 가장 일찍 끝나는 거 찾기
    # 그 일찍 끝나는거 이어서 바로 시작하거나 제일 가깝게 시작하는거 찾기
    # 단 찾을때 시작시간이 가까워도 끝나는 시간이 길어서 시작시간과 멀어도 끝나는 시간이 가까운 것을 선택하기
    # 그렇게 해서 연속으로 진행되는 회의 찾기
    st = arr[0][0]
    et = arr[0][1]
    cnt = 1
    tmp = 0
    for i in range(n):
        if arr[i][0] >= st and arr[i][1] < et:
            st = arr[i][0]
            et = arr[i][1]
        elif arr[i][0] >= et:
            cnt += 1
            st = arr[i][0]
            et = arr[i][1]
    print(cnt)
