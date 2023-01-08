def d(massive):
    massive = massive.replace(", ", "").replace("-", "")
    if massive.isdigit():
        return False
    else:
        return True
def sum(massive):
    summ = 0
    for i in range(0, len(massive)):
        summ += int(massive[i])
    return summ
def multi(massive):
    multip = 1
    for i in range(0, len(massive)):
        multip *= int(massive[i])
    return multip
listt = input()
if d(listt):
    print("error")
    exit(0)
massive = listt.split(",")
print("Сумма: " + str(sum(massive)))
print("Произведение: " + str(multi(massive)))
