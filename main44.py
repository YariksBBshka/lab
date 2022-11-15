n = int(input())
if n > 0:
    n += 1
    sum = 0
    for i in range(1, n):
        sum += i
    count = 2
    while n > count:
        en = int(input())
        sum -= en
        count += 1
    print(sum)
else:
    print("ERROR")