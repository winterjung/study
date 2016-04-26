#salamandersylph
def Powerset(s):
    A=[[]]
    for x in s[::-1]:
        A+=[[x]+y for y in A]
    return A
