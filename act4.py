def c(a, b):
    if b >= a:
        return 0.0
    return a - b

a = float(input("Enter the total bill amount: "))
b = float(input("Enter the amount paid by the customer: "))

d = c(a, b)

if d > 0:
    print("Due amount:", round(d, 2))
else:
    print("No due amount. The bill is fully paid.")
