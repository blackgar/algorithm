import sys

sys.stdin = open("input.txt")

# 퀵정렬 함수
# 해당 내용은 알고리즘 테스트 2주차 확인
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    rest = arr[1:]

    left = [x for x in rest if x <= pivot]
    right = [x for x in rest if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    arr1 = list(map(int, input().split()))
    m = int(input())
    arr2 = list(map(int, input().split()))
    # 배열은 그냥 더하면 합쳐지므로 합친후 퀵 정렬 진행
    arr = arr1 + arr2
    print(quick_sort(arr))