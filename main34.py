woc = int(input())  # width
loc = int(input())  # length
nop = woc * loc  # number of pieces
if (woc > 0) and (loc > 0):
    while True:
        reqnop = input().lower()  # required number of pieces
        if reqnop == "stop":
            print("%d pieces are left." % nop)
            break
        required = int(reqnop)
        if required >= 0:
            numreq = int(reqnop)
            nop = nop - numreq
            if nop < 0:
                print("No more cake left! You need %d pieces more." % abs(nop))
                break
        else:
            print("ERROR")
            break
else:
    print("ERROR")