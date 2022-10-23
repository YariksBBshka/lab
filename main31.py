while True:
    num = int(input())
    if ((num >= -300) and (num <= 300)) or ((num >= 1000) and (num <= 1600)):
        print("The number is: %d" % num)
        break
    else:
        print("Invalid number!")
