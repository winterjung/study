def taskMaker(source, challengeId):
    switch = []
    number = []
    for i in range(len(source)):
        for j in range(len(source[i])):
            if source[i][j] == "/":
                switch.append(i)
                break
    for i in range(len(switch)):
        tmp = source[switch[i]].split("//")
        #tmp[0] = Tab
        #tmp[1] = DB 3
        #tmp[2] = blaghasdf
        number.append(int(tmp[1].split(" ")[1]))
    for i in range(len(source)-1, -1, -1):
        for j in range(len(switch)-1, -1, -1):
            if i == switch[j]:
                if challengeId != number[j]:
                    source.pop(i)
    for i in range(len(source)-1, -1, -1):
        for j in range(len(source[i])):
            if source[i][j] == "/":
                tmp = source[i].split("//")
                source.pop(i-1)
                source.pop(i-1)
                source.insert(i-1, tmp[0]+tmp[2])
                return source
