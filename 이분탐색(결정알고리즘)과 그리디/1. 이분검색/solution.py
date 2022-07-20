import sys

sys.stdin = open("input.txt")

def binary_search(arr, start, end, target):
    mid = (start + end) // 2

    if arr[mid] == target:
        return mid+1

    elif target < arr[mid]:
        return binary_search(arr, start, mid-1, target)

    else:
        return binary_search(arr, mid+1, end, target)

T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    numbers.sort()

    print(binary_search(numbers, 0, len(numbers)-1, m))
