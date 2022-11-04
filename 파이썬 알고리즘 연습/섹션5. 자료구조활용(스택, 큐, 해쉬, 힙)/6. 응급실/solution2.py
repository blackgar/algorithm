import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    patient_list = [(i, v) for (i, v) in enumerate(list(map(int, input().split())))]
    patient = patient_list[m][1]
    answer = 0
    i = 0

    # any 안쓰고 lambda로 직접 그 값에 접근하는 방법
    while True:
        max_danger = max(patient_list, key=lambda n:n[1])[1]
        if patient_list[0][1] < max_danger:
            patient_list.append(patient_list.pop(0))
        elif patient_list[0][1] == max_danger:
            answer += 1
            if patient_list[0][0] == m:
                break
            else:
                patient_list.pop(0)
    # any함수 사용 방법
    while True:
        cur = patient_list.pop(0)
        if any(cur[1] < x[1] for x in patient_list):
            patient_list.append(cur)
        else:
            answer += 1
            if cur[0] == m:
                break
    print(answer)

