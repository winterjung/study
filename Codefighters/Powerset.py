'''
Author
Ayamin
2000
For the given set S its powerset is the set of all possible subsets of S.

Given an array of unique integers nums, your task is to return the powerset of its elements.

Implement an algorithm that does it in a depth-first search fashion. That is, for every integer in the set, we can either choose to take or not take it. At first, we choose NOT to take it, then we choose to take it.

Example

For nums = [1, 2], the output should be
Powerset(nums) = [[], [2], [1], [1, 2]].
Here's how the answer is obtained:
don't take element 1
----don't take element 2
--------add []
----take element 2
--------add [2]
take element 1
----don't take element 2
--------add [1]
----take element 2
--------add [1, 2]
For nums = [1, 2, 3], the output should be
Powerset(nums) = [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]].
[input] array.integer nums

Array of unique positive integers, 1 ≤ nums.length ≤ 10.

[output] array.array.integer

The powerset of nums.
'''
def Powerset(nums):
	answer = []
	items = nums[:]
	n = len(nums)
	aSet = []
	for i in range(n):
		aSet.append(None)
	ps(aSet, 0, 0, items, n, answer)
	return answer

def ps(aSet, aSetLen, current, items, n, answer):
	if current == n:
		tmp = []
		for i in range(aSetLen):
			tmp.append(aSet[i])
		answer.append(tmp)
	else:
		current += 1
		ps(aSet, aSetLen, current, items, n, answer)
		current -= 1
		aSet[aSetLen]=items[current]
		aSetLen += 1
		current += 1
		ps(aSet, aSetLen, current, items, n, answer)
