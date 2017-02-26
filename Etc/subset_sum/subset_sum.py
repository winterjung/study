# 다양한 subset sum problem의 해결방법
# 기본적으로 재귀형태를 띄며 subset_sum()의 경우엔
# 경우의 table을 만들고 걸러내는 방식


def subsetsum(array, num):
    if sum(array) == num:
        return array
    if len(array) > 1:
        for subset in (array[:-1], array[1:]):
            result = subsetsum(subset, num)
            if result is not None:
                return result


def positive_negative_sums(seq):
    P, N = 0, 0
    for e in seq:
        if e >= 0:
            P += e
        else:
            N += e
    return P, N


def subset_sum(seq, s=0):
    P, N = positive_negative_sums(seq)
    if not seq or s < N or s > P:
        return False
    n, m = len(seq), P - N + 1
    table = [[False] * m for x in range(n)]
    table[0][seq[0]] = True
    for i in range(1, n):
        for j in range(N, P+1):
            table[i][j] = seq[i] == j or table[i-1][j] or table[i-1][j-seq[i]]
    return table[n-1][s]


def is_subset_sum(l, n, target):
    if target == 0:
        return True
    if (n == 0) and (target != 0):
        return False

    if l[n-1] > target:
        return is_subset_sum(l, n-1, target)

    a = is_subset_sum(l, n-1, target)
    b = is_subset_sum(l, n-1, target-l[n-1])
    return a or b
