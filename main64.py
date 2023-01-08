def localip(massive):
    for i in range(0, len(massive)):
        if int(massive[i]) == 10 and int(massive[i + 1]) == 0:
            return False
        elif int(massive[i]) == 172 and int(massive[i + 1]) == 16:
            return False
        elif int(massive[i]) == 192 and int(massive[i + 1]) == 168:
            return False
        else:
            return True

def dec(massive):
    decimalIP = 0
    for i in range(0, len(massive)):
        decimalIP += int(massive[i]) * (256 ** (3 - i))
    return decimalIP

n = int(input())
if n < 1:
    print("error")
    exit(0)
stack = []
i = 0
flag = False
flagg = False
while n > i:
    stack = input().split(".")
    for j in range(0, len(stack)):
        if int(stack[j]) < 0 or int(stack[j]) > 255:
            if int(stack[1]) == 0:
                print("error")
                exit(0)
            if int(stack[j]) == 255:
                flagg = True
            print("error")
            exit(0)
    if len(stack) != 4 or flagg == True:
        print("error")
        exit(0)
    if localip(stack) == True:
        stack.append((stack))
    else:
        flag = True
    i += 1

n += 1
stack.append("")
mod = [i for i in range(0, n - 1)]
flagg = False
if not flag:
    while not flagg:
        for l in range(0, n - 1):
            if dec(stack[l]) > dec(stack[l + 1]):
                mod[l] = stack[l]
                stack[l] = stack[l + 1]
                stack[l + 1] = mod[l]
            for i in range(0, n - 1):
                if dec(stack[l]) >= dec(stack[l + 1]):
                    flagg = True
                else:
                    flagg = False
        for k in range(0, n):
            if stack[k] != "":
                print(".".join(stack[k]))
        exit(0)
else:
    print("The list contains the local IP!")
