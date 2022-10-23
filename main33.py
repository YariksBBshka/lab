n = int(input()) # Вводимое кол-во чисел
if n>0:
    count = 1 # Счётчик для цикла
    minimum = 10000000000
    while count <= n:
        im = int(input())
        if im < minimum:
            minimum = im
        count += 1
    print(minimum)
else:
    print("ERROR")
