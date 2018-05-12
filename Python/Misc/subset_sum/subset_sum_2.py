import csv
import numpy as np
from itertools import chain, combinations

MAX_COMBO = 5


def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(MAX_COMBO+1))


# 데이터 로딩
source = []
source_value = []
source_title = []

target = []
target_value = []
target_title = []

with open("source_cutting.csv", encoding="utf-8") as source_file:
    rows = csv.reader(source_file, delimiter=",")
    for row in rows:
        source.append(row)
    source.pop(0)
    source = sorted(source, key=lambda x: x[1])
    source = np.array(source)

with open("target_cutting.csv", encoding="utf-8") as source_file:
    rows = csv.reader(source_file, delimiter=",")
    for row in rows:
        target.append(row)
    target.pop(0)
    target = sorted(target, key=lambda x: x[1])
    target = np.array(target)

# 데이터 변환 (분리, 문자->숫자)
source_title = source.T[0]
source_value = source.T[1].astype("int")
target_title = target.T[0]
target_value = target.T[1].astype("int")

for i, goal in enumerate(target_value, 1):
    used_source = source_value[source_value <= goal]
    print("============ {}/{} ============".format(i, len(target_value)))
    print("target : {}".format(goal))
    print("source : {}/{}".format(len(used_source), len(source_value)))

    counter = 0
    for i, combo in enumerate(powerset(used_source), 1):
        result = sum(combo)
        if result == goal:
            counter += 1
            # print("#{:5d} {}".format(i, combo))
    print("total {} found!".format(counter))
    # break