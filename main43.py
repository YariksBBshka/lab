n = int(input())
if n == 1:
    firstsum = int(input())
    secondsum = int(input())
    sumofpair = firstsum + secondsum
    print("Yes, value = %.f" % sumofpair)
elif n > 0:
    count = 1
    maxdif = -111111111
    firstsum = int(input())
    secondsum = int(input())
    sumofpair = firstsum + secondsum
    while count < n:
        firstsum = int(input())
        secondsum = int(input())
        sumofpair2 = firstsum + secondsum
        dif = abs(sumofpair2 - sumofpair)
        if (dif > maxdif):
            maxdif = dif
            sumofpair = sumofpair2
        count += 1
    if maxdif == 0:
        print("Yes, value = %.f" % sumofpair)
    else:
        print("No, maxdiff = %.f" % maxdif)
else:
    print("ENTER NUMBER OF PAIRS MORE THAN ZERO")
