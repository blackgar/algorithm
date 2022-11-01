import sys

sys.stdin = open("input.txt")

def check_vertical_sudoku(line):
    #1 아래 처럼 값의 개수를 비교하는 방법
    for i in range(1, 10):
        if line.count(i) > 1 or line.count(i) == 0:
            return False
    #2 배열을 비교하는 방법
    number = [num for num in range(1, 10)]
    sorted_line = sorted(line)
    if number != sorted_line:
        return False
    return True

def check_square_sudoku(arr):
    # 8방향 값을 체크하기 위한 방향 인덱스
    dx = [0, 1, 0, -1, 1, 1, -1, -1]
    dy = [1, 0, -1, 0, -1, 1, 1, -1]
    # 3*3 스도쿠의 중앙에서 8방향으로 체크하면 되므로 1, 4, 7 인덱스 활용
    for y in range(1, 9, 3):
        for x in range(1, 9, 3):
            # 한줄의 배열로 체크하기 위해 만들어줄 임시 변수
            tmp_sudoku = [arr[y][x]]
            # 8방향 체크후 각 값을 임시 배열에 넣기
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                tmp_sudoku.append(arr[ny][nx])
            # 완성된 한줄 배열을 check_vertical_sudoku라는 함수에 넣어서 체크해서
            # 만약 sukoku가 아니면 False를 맞으면 계속 반복문을 돌아 모두 체크한 후 True 반환
            if not check_vertical_sudoku(tmp_sudoku):
                return False

    return True

T = int(input())

for tc in range(1, T + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    sudoku_reverse = []
    is_sudoku = "YES"
    # 세로줄 배열을 따로 가로 배열로 변환해주기
    for i in zip(*sudoku):
        sudoku_reverse.append(i)
    # 세로줄과 가로줄 모두 sudoku의 조건을 만족하는지 체크하는 부분
    for i in range(9):
        if not (check_vertical_sudoku(sudoku[i]) and check_vertical_sudoku(sudoku_reverse[i])):
            is_sudoku = "NO"
            break
    # 3*3 격자판이 스도쿠인지 체크하는 부분
    if not check_square_sudoku(sudoku):
        is_sudoku = "NO"

    print(is_sudoku)