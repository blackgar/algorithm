import sys

sys.stdin = open("input.txt")

# 주사위 눈의 개수를 세어줄 함수
def count_number(arr):
    # 주사위 눈 인덱스와 맞추기 위해 길이 7의 배열 선언
    count_list = [0]*7
    # 주사위 눈에 맞게 해당 배열에 + 1
    for i in arr:
        count_list[i] += 1
    # 최종 배열 반환
    return count_list

# 총 상금을 계산해주는 함수
def check_reward(arr):
    # 주사위 눈을 세어준 배열 반환 받기
    count_list = count_number(arr)
    # 그 중 제일 많이 나온 눈의 개수
    max_count = max(count_list)
    # 만약 3개면 모두 같은 주사위 눈이 나왔다는 것이므로 1등 상금 지급
    # count_list의 max값이 있는 곳의 인덱스가 곧 그 주사위 눈이 되는 원리 이용
    if max_count == 3:
        return count_list.index(max(count_list)) * 1000 + 10000
    elif max_count == 2:
        return count_list.index(max(count_list)) * 100 + 1000
    # 모두 다른 눈이 나왔을 때는 내장 함수 max값이 제일 처음 찾아진 수의 인덱스를 가져오므로 직접 for문을 통해
    # 뒤에서 부터 찾아 나온 주사위 눈 중 가장 큰 수로 상금을 계산할 수 있도록 구현
    else:
        for i in range(6, 0, -1):
            if count_list[i] == 1:
                return i * 100

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    answer = 0
    # 주사위 숫자를 받아서 상금을 check하고 max값 대조를 통해 제일 큰 상금 출력할 수 있도록 구현
    for i in range(n):
        dice_num = list(map(int, input().split()))
        reward = check_reward(dice_num)
        if reward > answer:
            answer = reward

    print(answer)