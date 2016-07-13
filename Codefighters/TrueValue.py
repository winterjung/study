def TrueValue(num):
    if num < 10:
        return num
    else:
        num2 = str(num)
        mul = len(num2)
        sum_ = 0
        for i in range(len(num2)):
            sum_ += mul*int(num2[i])
            mul -= 1
            print(sum_, mul)
        print("---------")
        return TrueValue(sum_)

print("Test Case :", TrueValue(10230918))
