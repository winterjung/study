def lastTwo(n, k):
    base = 1
    master = []
    master.append(n % 10)
    master.append((n % 100) // 10)
    slave = master[:]
    pattern = []
    if k < 100:
        loop = k-1
    else:
        loop = 100
    for i in range(loop):
        base = (master[0] * slave[0]) + (master[0] * slave[1] * 10) + (master[1] * slave[0] * 10)
        slave[1] = (base % 100) // 10
        slave[0] = base % 10
        pattern.append(str(slave[1]) + str(slave[0]))
        if i > 0:
            if pattern[0] == pattern[i]:
                if k % i < 2:
                    return pattern[(k % i) +i-2]
                return pattern[(k % i) -2]
    return str(slave[1]) + str(slave[0])
