import sys

balance = 0
while True:
    country = str(input()).lower()
    if country == "end":
        break
    country = country[0].upper() + country[1:]
    req = str(input().lower())
    if req == "end":
        break
    requiredsum = int(req)
    if requiredsum < 0:
        print("HOW???")
        break
    while (balance < requiredsum):
        income = str(input())
        if income == "end":
            sys.exit()
        incomesum = int(income)
        if incomesum < 0:
            print("DON'T WASTE MONEY FROM TRAVEL BUDGET")
        balance += incomesum
    balance -= requiredsum
    if balance >= 0:
        print("Going to " + country)


