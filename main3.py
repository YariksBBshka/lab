area = float(input())
costWithOutDiscount = area * 7.61
discount = costWithOutDiscount * 0.18
print("The final price is: %.2f $." % (costWithOutDiscount - discount))
print("The discount is: %.2f $." % discount)