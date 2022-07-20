import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [int(input()) for _ in range(n)]
    answer = 0

    # 4개를 같은 길이로 잘라서 m개 이상이 되는지 체크하기
    # 잘랐는데 m개 이하다 그럼 그 숫자 이후로는 절대 못자르는거임
    s = min(arr)
    e = max(arr)
    while True:
        mid = (s+e) // 2
        cnt = 0
        for i in range(n):
            cnt += arr[i] // mid
            if cnt == m:
                break
        if cnt == m:
            for i in range(mid, e+1, 1):
                tmp = 0
                for j in range(n):
                    tmp += arr[j] // i
                    if tmp > m:
                        break
                if tmp < m:
                    answer = i-1
                    break
            break
        if cnt < m:
            e = mid - 1
        else:
            s = mid + 1
    print(answer)

    # k = sum(arr) // m
    # length = min(arr)
    # while True:
    #     cnt = 0
    #     for i in range(n):
    #         cnt += arr[i]//length
    #         if cnt >= m:
    #             break
    #     if cnt < m:
    #         for i in range(length-k, length, 1):
    #             cnt = 0
    #             for j in range(n):
    #                 cnt += arr[j]//i
    #                 if cnt >= m:
    #                     break
    #             if cnt < m:
    #                 length = i
    #                 break
    #         break
    #     length += k
    # print(length)


    # k = max(arr)
    # cnt = 0
    # for i in range(k, 0, -1):
    #     for j in range(len(arr)):
    #         cnt += arr[j] // k
    #         if cnt > m:
    #             answer = i
    #             break
    #     if cnt > m:
    #         break
    # print(answer)

