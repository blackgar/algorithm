import sys

sys.stdin = open("input.txt")

def reverse(x):
    # 문자열을 쉽게 계산해서 뒤집기 위해 배열을 통해
    # 임시로 값을 저장해준다.
    tmp = []
    # 문자열을 리스트로 변환해주고
    for i in x:
        tmp.append(i)
    # 리스트 뒤집어서 뒤집은 수 만들어주고
    tmp.reverse()
    # 0이 연속되면 그 부분 만큼 자르고 남은 수로
    # 계산 진행하기 위해 슬라이스 활용
    # 0이 있으면 그 다음으로 넘어가고
    # 0이 없으면 그 수부터 제일 끝까지 수를
    # 이용해서 계산하면 되므로 슬라이싱 아래처럼 이용
    for j in range(len(tmp)):
        if tmp[j] == "0":
            continue
        else:
            tmp = tmp[j:]
            break
    # join으로 문자열로 다시 만들어주고
    numbers = ''.join(tmp)
    # 소수의 기준이 되는지 체크하고
    if int(numbers) < 2:
        return 0
    # 2이상의 수에 한해 소수인지 판별해서 해당 수를
    # 리턴해주는 함수
    if isPrime(int(numbers)):
        return int(numbers)
    else:
        return 0

def isPrime(x):
    # 단순한 소수 계산
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    result = []
    # for문 돌면서 숫자 하나하나 계산하고 만약 해당 수가 반환되면
    # 리스트에 담아서 출력해주기.
    for i in range(n):
        if reverse(str(arr[i])):
            result.append(reverse(str(arr[i])))
    print(*result)
