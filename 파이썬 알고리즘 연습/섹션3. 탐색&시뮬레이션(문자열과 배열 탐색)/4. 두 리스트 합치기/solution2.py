import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    arr1 = list(map(int, input().split()))
    m = int(input())
    arr2 = list(map(int, input().split()))
    sorted_arr = []
    arr1_index = 0
    arr2_index = 0

    while arr1_index < n or arr2_index < m:
        if arr1_index < n and arr2_index < m:
            if arr1[arr1_index] <= arr2[arr2_index]:
                sorted_arr.append(arr1[arr1_index])
                arr1_index += 1
            else:
                sorted_arr.append(arr2[arr2_index])
                arr2_index += 1
        elif arr1_index >= n:
            sorted_arr += arr2[arr2_index:]
            break
        elif arr2_index >= m:
            sorted_arr += arr1[arr1_index:]
            break

    print(sorted_arr)
