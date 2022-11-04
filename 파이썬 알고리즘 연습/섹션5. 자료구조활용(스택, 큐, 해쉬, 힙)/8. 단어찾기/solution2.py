import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    word_list = [input() for _ in range(n)]
    poem_word = [input() for _ in range(n-1)]

    # 정렬 활용 방법
    word_list.sort()
    poem_word.sort()
    for i in range(n):
        if i == n-1:
            print(word_list[i])
        if word_list[i] != poem_word[i]:
                print(word_list[i])
                break


    # 정렬 x, 딕셔너리 활용
    dictionary = dict()
    for i in word_list:
        dictionary[i] = 1
    for i in poem_word:
        dictionary[i] = 0
    for key, val in dictionary.items():
        if val == 1:
            print(key)
            break




