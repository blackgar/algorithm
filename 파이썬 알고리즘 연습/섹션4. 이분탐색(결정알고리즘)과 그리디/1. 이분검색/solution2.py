import sys

sys.stdin = open("input.txt")

# 이분검색 함수
def binary_search(arr, start, end, target):
    # 중간지점
    mid = (start + end) // 2
    # 중간지점의 수가 목표 보다 작으면 중간지점에서 오른쪽 구간을 찾고
    if arr[mid] < target:
        return binary_search(arr, mid+1, end, target)
    # 중간지점의 수가 목표 보다 크면 중간지점에서 왼쪽 구간을 찾고
    elif arr[mid] > target:
        return binary_search(arr, start, mid, target)
    # 중간지점의 수가 목표랑 같으면 위치는 +1이므로 현재 인덱스 +1을 반환해준다.
    else:
        return mid+1

T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()

    print(binary_search(arr, 0, n-1, m))