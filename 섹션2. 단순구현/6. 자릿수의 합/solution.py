import sys

sys.stdin = open("input.txt")

def digit_sum(x, nums):
    # tmp를 통해 리스트안의 숫자 자리수 별로 int로 변환해서 계산
    # 계산해서 result라는 배열에 숫자를 넣어준다.
    result = []
    for i in range(x):
        tmp = 0
        for j in range(len(nums[i])):
            tmp += int(nums[i][j])
        result.append(tmp)
        # numbers와 result는 같은 index를 공유하기 때문에
        # result가 가장 큰 곳의 index의 numbers가 가장 자리수 합이 큰 수이고
        # index 메서드 자체가 가장 앞에서부터 찾기 때문에 입력순으로 먼저인 수 출력 가능
    return nums[result.index(max(result))]

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    # 문자열로 숫자들을 리스트로 입력받기
    numbers = list(input().split())

    print(digit_sum(n, numbers))