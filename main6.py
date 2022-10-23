fruit = input().lower()
dotw = input().lower()
kg = float(input())
if (kg>0):
    if dotw == 'monday' or dotw == 'tuesday' or dotw == 'wednesday' or dotw == 'thursday' or dotw == 'friday':
        if fruit == 'banana':
            print('%.2f' % (2.50 * kg))
        elif fruit == 'apple':
            print('%.2f' % (1.20 * kg))
        elif fruit == 'orange':
            print('%.2f' % (0.85 * kg))
        elif fruit == 'grapefruit':
            print('%.2f' % (1.45 * kg))
        elif fruit == 'kiwi':
            print('%.2f' % (2.70 * kg))
        elif fruit == 'pineapple':
            print('%.2f' % (5.50 * kg))
        elif fruit == 'grapes':
            print('%.2f' % (3.85 * kg))
        else:
            print("ERROR")
    elif dotw == 'saturday' or dotw == 'sunday':
        if fruit == 'banana':
            print('%.2f' % (2.70 * kg))
        elif fruit == 'apple':
            print('%.2f' % (1.25 * kg))
        elif fruit == 'orange':
            print('%.2f' % (0.90 * kg))
        elif fruit == 'grapefruit':
            print('%.2f' % (1.60 * kg))
        elif fruit == 'kiwi':
            print('%.2f' % (3.00 * kg))
        elif fruit == 'pineapple':
            print('%.2f' % (5.60 * kg))
        elif fruit == 'grapes':
            print('%.2f' % (4.20 * kg))
        else:
            print("ERROR")
    else:
        print("ERROR")
else:
    print("ERROR")