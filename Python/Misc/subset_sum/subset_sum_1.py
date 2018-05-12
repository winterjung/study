from itertools import chain, combinations
import csv
import numpy as np

MAX_COMBO = 5


def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(MAX_COMBO+1))


nums = []
with open("source_cutting.csv", encoding="utf-8") as source_file:
    rows = csv.reader(source_file, delimiter=",")
    for row in rows:
        nums.append(row)
    nums.pop(0)
    nums = sorted(nums, key=lambda x: x[1])
    nums = np.array(nums)

source_title = nums.T[0]
source_value = nums.T[1].astype("int")

inputSum = 32917520

nums_filter = set([n for n in source_value if n <= inputSum])
print("nums : {}, filtered : {}".format(len(source_value), len(nums_filter)))
for i, combo in enumerate(powerset(nums_filter), 1):
    if sum(combo) == inputSum:
        print(combo)
