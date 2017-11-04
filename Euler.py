def problem1 ():
    divThreeSum = 0
    divFiveSum = 0
    divFifteenSum = 0
    for i in range(1,1000):
        if (i % 3 == 0 & i % 5 == 0):
            divThreeSum += i
            divFiveSum += i
            divFifteenSum += i
        elif (i % 3 == 0):
            divThreeSum += i
        elif (i % 5 == 0):
            divFiveSum += i
    result = divThreeSum + divFiveSum - divFifteenSum
    return (result)

def problem2 ():
    a = 1
    b = 2
    c = 3
    fibsum = 0
    while(a <= 4000000):
        temp = b + c
        a = b
        b = c
        c = temp
        if (a % 2 == 0):
            fibsum += a
    return (fibsum)
