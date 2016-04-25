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
