import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    answer = 0
    # 조용필의 앨범 곡들이 주어진다.
    # 각 곡들은 순서대로 DVD에 들어갈 수 있다.
    # 들어갈 DVD는 모두 동일하다.
    # m개의 DVD에 녹화할 수 있는 최대 크기를 찾는다.

    # 현재 배열에 들어있는 값들 중 제일 최대 값이 DVD 최소 값이 된다.(최대 값부터 찾기 시작 10001까지)
    # 배열을 돌면서 최대값의 DVD에 첫 곡부터 넣으면서 DVD 값을 초과하면 다음 곡을 넣는 방식으로 넣어서
    # 다 넣지 않았는데 cnt가 m을 넘어가면 다음 크기의 DVD에 넣는 방식으로 진행
    # 만약에 특정 차례의 DVD에 곡을 넣고 남은 길이를 살펴 봤는데 남은 값들의 개수와 남은 잔여 DVD가 일치하면
    # 그 때는 뒤에 있는 것들을 하나씩 넣으면 되니까 그냥 cnt에 +남은양 하면 된다. answer에 기록
    # 이렇게 정답에 기록해두고 cnt == m인 구간을 찾게 되면 답을 answer에 기록한다.
    # 이렇게 숫자를 계속 늘려가다가 cnt < m인 구간이 오게 되면 이 전 값이 정답이 된다.

    for i in range(max(arr), 10001):
        tmp = 0
        cnt = 0
        print("first", tmp, cnt, i)
        for j in range(n-1):
            tmp += arr[j]
            # 다음 노래가 들어왔을 때 현재 DVD가 못 담는다면 + 1해주고 다음 DVD로 리셋
            if tmp + arr[j+1] > i:
                print("second", arr[j], tmp, cnt, answer)
                cnt += 1
                tmp = 0
            if j == n-2:
                cnt += 1
            if n-j-1 == m-cnt:
                answer = i
                break
            if cnt >= m:
                answer = i
                break



            # tmp += arr[j]
            # print("second", arr[j], tmp, cnt, answer)
            # if tmp > i:
            #     print("크다")
            #     tmp = arr[j]
            #     cnt += 1
            # elif tmp == i:
            #     print("같다")
            #     tmp = 0
            #     cnt += 1
            # if j == n-1:
            #     cnt += 1
            # if n - j - 1 == m - cnt:
            #     print("남은거에 다 들어가는데요?")
            #     answer = i
            #     break
            # if cnt >= m:
            #     print("넘쳤다.")
            #     answer = i
            #     break
        if cnt < m:
            break

    print(answer)