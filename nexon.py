'''
어떤 자연수 n이 있을 때, d(n)을 n의 각 자릿수 숫자들과 n 자신을 더한 숫자라고 정의하자.

예를 들어
d(91) = 9 + 1 + 91 = 101
이 때, n을 d(n)의 제네레이터(generator)라고 한다. 위의 예에서 91은 101의 제네레이터이다.

어떤 숫자들은 하나 이상의 제네레이터를 가지고 있는데, 101의 제네레이터는 91 뿐 아니라 100도 있다.
그런데 반대로, 제네레이터가 없는 숫자들도 있으며,
이런 숫자를 인도의 수학자 Kaprekar가 셀프 넘버(self-number)라 이름 붙였다.
예를 들어 1,3,5,7,9,20,31 은 셀프 넘버 들이다.

1 이상이고 5000 보다 작은 모든 셀프 넘버들의 합을 구하라.
'''

import time


def generator(n):
    strN = str(n)
    dn = sum([int(i) for i in list(strN)]) + n
    return dn


def no_selfnum(num):
    return sum([int(n) for n in str(num)]) + num


# version 1
generators = []
check = list(range(1, 5000))

t1 = time.time()
for i in range(1, 5000):
    dn = generator(i)
    if dn not in generators:
        generators.append(dn)

for n in generators:
    if n in check:
        check.remove(n)
t2 = time.time()
print("time : %2f" % (t2-t1))

# version 2
check = list(range(1, 5000))

t1 = time.time()
for i in range(1, 5000):
    dn = generator(i)
    if dn in check:
        check.remove(dn)
t2 = time.time()
print("time : %2f" % (t2-t1))

# version 3
max_num = 5000

t1 = time.time()
result = sum(set(range(1, max_num + 1)) - {no_selfnum(num) for num in range(1, max_num + 1)})
t2 = time.time()
print("time : %2f" % (t2-t1))
