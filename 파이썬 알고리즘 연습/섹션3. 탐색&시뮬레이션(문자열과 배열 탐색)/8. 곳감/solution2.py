import sys

sys.stdin = open("input.txt")

def rotate(arr, direction, times):
    n = len(arr)
    new_arr = [0] * n
    # 길이 이상으로 이동하라는 것은 결국 제자리로 돌아온 후 나머지 만큼 이동하라는 것과 같으므로 나머지 연산자로 계산
    times %= n
    # 예를 들어 7*7격자에서 한 줄이 들어왔다. 왼쪽 & 오른쪽으로 구분짓는다
    # 왼쪽의 경우 왼쪽으로 3번 가라는 경우 현재
    # index - times 하게 되면 현재 index가 1인 경우 -2로 끝에서 두번째로 이동해서 위치가 맞게 된다.
    if direction == 0:
        for i in range(n):
            new_arr[i-times] = arr[i]
        return new_arr
    # 오른족의 경우 오른쪽으로 3회 이동하라는 경우
    # 현재 index + times % len(arr) 해주면 현재 index가 5인 경우 8 % 7로 1의 위치로 이동
    else:
        for i in range(n):
            new_arr[(i+times)%n] = arr[i]
        return new_arr

def count_gotgam(arr):
    n = len(arr)
    mid = n // 2
    hap = 0
    # 위에 줄어드는 깔대기 모양으로 계산
    for i in range(mid+1):
        hap += sum(arr[i][i:n-i])
    # 아래 늘어나는 깔대기 모양 계산
    for i in range(mid-1, -1, -1):
        hap += sum(arr[n-i-1][i:n-i])
    return hap




T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    m = int(input())
    rotate_command = [list(map(int, input().split())) for _ in range(m)]
    # 회전 명령에 맞게 회전 함수로 배열 회전
    for i in range(m):
        arr[rotate_command[i][0]-1] = rotate(arr[rotate_command[i][0]-1], rotate_command[i][1], rotate_command[i][2])
    # 이후 곶감 개수를 센 후 출력
    print(count_gotgam(arr))

