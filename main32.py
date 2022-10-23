n = int(input()) # Вводимое кол-во чисел
if n>0:
    count = 1 # Счётчик для цикла
    maximum = -10000000000
    while count <= n:
        im = int(input())
        if im > maximum:
            maximum = im
        count += 1
    print(maximum)
else:
    print("ERROR")
