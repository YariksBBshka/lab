count = 0
pnsum = 0
npnsum = 0
while True:
    command = str(input().lower())
    if command == "stop":
        print("Sum of all prime numbers is: %.f" % pnsum)
        print("Sum of all non-prime numbers is: %.f" % npnsum)
        break
    enterednum = int(command)
    if enterednum < 0:
        print("Number is negative")
    elif enterednum == 0:
        print("Number is zero")
    elif enterednum == 1:
        print("Number is neither prime nor non-prime")
    else:
        for d in range(1, 100000000, 1):
            if enterednum % d == 0:
                count += 1
        if count == 2:
            pnsum += enterednum
        elif count > 2:
            npnsum += enterednum
        count = 0
