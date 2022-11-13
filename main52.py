n = int(input())
n += 1
for line in range(1, n):
    count = 1
    while count < line:
        print("*", end='\t')
        count += 1
    for column in range(count, n):
        print(column, end='\t')
    print()
