# seq1 = "AGATAGATAGAATGATT"
# seq2 = "AA"

# 주어진 input 값
seq1 = "CTTGGTACACGGAACGTTCTGAAAAGAGCTATGAATTGCAGACACCTTTTGAAATTAAATTGGCAAAGAAATTTGACACCTTCAATGGGGAATGTCCAAATTTTGTATTTCCCTTAAATTCCATAATCAAGACTATTCAACCAAGGGTTGAAAAGAAAAAGCTTGATGGCTTTATGGGTAGAATTCGATCTGTCTATCCAGTTGCGTCACCAAATGAATGCAACCAAATGTGCCTTTCAACTCTCATGAAGTGTGATCATTGTGGTGAAACTTCATGGCAGACGGGCGATTTTGTTAAAGCCACTTGCGAATTTTGTGGCACTGAGAATTTGACTAAAGAAGGTGCCACTACTTGTGGTTACTTACCCCAAAATGCTGTTGTTAAAATTTATTGTCCAGCATGTCACAATTCAGAAGTAGGACCTGAGCATAGTCTTGCCGAATACCATAATGAATCTGGCTTGAAAACCATTCTTCGTAAGGGTGGTCGCACTATTGCCTTTGGAGGCTGTGTGTTCTCTTATGTTGGTTGCCATAACAAGTGTGCCTATTGGGTTCCACGTGCTAGCGCTAACATAGGTTGTAACCATACAGGTGTTGTTGGAGAAGGTTCCGAAGGTCTTAATGACAACCTTCTTGAAATACTCCAAAAAGAGAAAGTCAACATCAATATTGTTGGTGACTTTAAACTTAATGAAGAGATCGCCATTATTTTGGCATCTTTTTCTGCTTCCACAAGTGCTTTTGTGGAAACTGTGAAAGGTTTGGATTATAAAGCATTCAAACAAATTGTTGAATCCTGTGGTAATTTTAAAGTTACAAAAGGAAAAGCTAAAAAAGGTGCCTGGAATATTGGTGAACAGAAATCAATACTGAGTCCTCTTTATGCATTTGCATCAGAGGCTGCTCGTGTTGTACGATCAATTTTCTCCCGCACTCTTGAAACTGCTCAAAATTCTGTGCGTGTTTTACAGAAGGCC"
seq2 = "AGATGCG"

# seq2의 길이(클린 코드를 위해)
n = len(seq2)
# 가장 낮은 hamming distance를 담아 비교하기 위한 변수(최대 distance를 담아 놓은 상태에서 비교 시작)
lowest_hamming_distance = n
# 가장 낮은 hamming distance를 가지는 문자열 seq1상의 위치를 담을 배열
location = []

# 문자열 seq1을 순회하면서 마지막 seq2의 길이만큼 단어를 비교할 수 있을 때까지를 반복문 범위로 지정
for i in range(len(seq1)-n+1):
    # seq1과 seq2의 다른 문자의 개수를 담아 주기 위한 변수
    # 비교가 끝나고 다음 반복문이 시작될 때 초기화되게끔 지정
    print(seq1[i:i+n])
    print(seq2)
    cnt = 0
    # 비교 위치를 하나씩 오른쪽으로 옮겨가면서 비교 하면서 cnt를 하나씩 늘려준다.
    for x in range(n):
        if seq1[i+x] != seq2[x]:
            cnt += 1
    print("lowest hamming didstance", lowest_hamming_distance)
    print("current hamming distance", cnt)

    # 만약 현재 확인된 가장 낮은 hamming distance와 같다면 위치를 여러개 출력해야 되므로 배열 location에 추가
    if cnt == lowest_hamming_distance:
        location.append(i+1)
    # 만약 현재 확인된 가장 낮은 hamming distance보다 작다면 현재 cnt가 가장 낮은 hamming distance 이므로 값 갱신 후
    # 기존에 담겨 있던 위치의 배열을 현재 위치를 담은 배열로 초기화 시켜준다.
    elif cnt < lowest_hamming_distance:
        lowest_hamming_distance = cnt
        location = [i+1]
    print("location", location)
# location 배열에 담겨 있는 가장 낮은 hamming distanace를 가지는 문자열의 위치를 출력한다.
print(*location)
