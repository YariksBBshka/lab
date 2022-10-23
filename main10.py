budget = int(input())
season = str(input().lower())
nop = int(input())
if (budget>=1) and (budget<=8000):
    if (nop>=4) and (nop<=18):
        if season == "spring":
            if (nop >= 4) and (nop <= 6):
                if (nop % 2 == 0):
                    remainder = (budget - 3000 * 0.85)
                elif (nop % 2 == 1):
                    remainder = (budget - 3000 * 0.90)
                    if remainder > 0:
                        print("Yes! You have %.2f rubles left" % remainder)
                    else:
                        remainder = abs(remainder)
                        print("Not enough money! You need %.2f rubles" % remainder)
            if (nop >= 7) and (nop <= 11):
                if (nop % 2 == 0):
                    remainder = (budget - 3000 * 0.80)
                elif (nop % 2 == 1):
                    remainder = (budget - 3000 * 0.85)
                    if remainder > 0:
                        print("Yes! You have %.2f rubles left" % remainder)
                    else:
                        remainder = abs(remainder)
                        print("Not enough money! You need %.2f rubles" % remainder)
            if (nop >= 12):
                if (nop % 2 == 0):
                    remainder = (budget - 3000 * 0.70)
                elif (nop % 2 == 1):
                    remainder = (budget - 3000 * 0.75)
                    if remainder > 0:
                        print("Yes! You have %.2f rubles left" % remainder)
                    else:
                        remainder = abs(remainder)
                        print("Not enough money! You need %.2f rubles" % remainder)
        elif season == "winter":
            if (nop >= 4) and (nop <= 6):
                if (nop % 2 == 0):
                    remainder = (budget - 2600 * 0.85)
                elif (nop % 2 == 1):
                    remainder = (budget - 2600 * 0.90)
                    if remainder > 0:
                        print("Yes! You have %.2f rubles left" % remainder)
                    else:
                        remainder = abs(remainder)
                        print("Not enough money! You need %.2f rubles" % remainder)
            if (nop >= 7) and (nop <= 11):
                if (nop % 2 == 0):
                    remainder = (budget - 2600 * 0.80)
                elif (nop % 2 == 1):
                    remainder = (budget - 2600 * 0.85)
                    if remainder > 0:
                        print("Yes! You have %.2f rubles left" % remainder)
                    else:
                        remainder = abs(remainder)
                        print("Not enough money! You need %.2f rubles" % remainder)
            if (nop >= 12):
                if (nop % 2 == 0):
                    remainder = (budget - 2600 * 0.70)
                elif (nop % 2 == 1):
                    remainder = (budget - 2600 * 0.75)
                    if remainder > 0:
                        print("Yes! You have %.2f rubles left" % remainder)
                    else:
                        remainder = abs(remainder)
                        print("Not enough money! You need %.2f rubles" % remainder)
        elif season == "summer":
            if (nop >= 4) and (nop <= 6):
                if (nop % 2 == 0):
                    remainder = (budget - 4200 * 0.85)
                elif (nop % 2 == 1):
                    remainder = (budget - 4200 * 0.90)
                    if remainder > 0:
                        print("Yes! You have %.2f rubles left" % remainder)
                    else:
                        remainder = abs(remainder)
                        print("Not enough money! You need %.2f rubles" % remainder)
            if (nop >= 7) and (nop <= 11):
                if (nop % 2 == 0):
                    remainder = (budget - 4200 * 0.80)
                elif (nop % 2 == 1):
                    remainder = (budget - 4200 * 0.85)
                    if remainder > 0:
                        print("Yes! You have %.2f rubles left" % remainder)
                    else:
                        remainder = abs(remainder)
                        print("Not enough money! You need %.2f rubles" % remainder)
            if (nop >= 12):
                if (nop % 2 == 0):
                    remainder = (budget - 4200 * 0.70)
                elif (nop % 2 == 1):
                    remainder = (budget - 4200 * 0.75)
                    if remainder > 0:
                        print("Yes! You have %.2f rubles left" % remainder)
                    else:
                        remainder = abs(remainder)
                        print("Not enough money! You need %.2f rubles" % remainder)
        elif season == "autumn":
            if (nop >= 4) and (nop <= 6):
                remainder = (budget - 4200 * 0.90)
                if remainder > 0:
                    print("Yes! You have %.2f rubles left" % remainder)
                else:
                    remainder = abs(remainder)
                    print("Not enough money! You need %.2f rubles" % remainder)
            if (nop >= 7) and (nop <= 11):
                remainder = (budget - 4200 * 0.85)
                if remainder > 0:
                    print("Yes! You have %.2f rubles left" % remainder)
                else:
                    remainder = abs(remainder)
                    print("Not enough money! You need %.2f rubles" % remainder)
            if (nop >= 12):
                remainder = (budget - 4200 * 0.75)
                if remainder > 0:
                    print("Yes! You have %.2f rubles left" % remainder)
                else:
                    remainder = abs(remainder)
                    print("Not enough money! You need %.2f rubles" % remainder)
        else:
            print("ERROR")
    else:
        print("ERROR")
else:
    print("ERROR")