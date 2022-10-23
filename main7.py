displaytype = str(input()).lower()
linecount = int(input())
columncount = int(input())
if (linecount >= 0) and (columncount >= 0):
    if displaytype == 'premiere':
        print("%.2f $" % (12 * linecount * columncount))
    elif displaytype == 'normal':
        print("%.2f $" % (7.50 * linecount * columncount))
    elif displaytype == 'discount':
        print("%.2f $" % (5 * linecount * columncount))
    else:
        print("ERROR, TRY TO ENTER DATA AGAIN")
else:
    print("ERROR, TRY TO ENTER DATA AGAIN")