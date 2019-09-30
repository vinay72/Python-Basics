hrs = input("Enter Hours:")
h = int(hrs)
rate = input("Enter Rate:")
r = float(rate)
total = 0
if (h >= 40):
    total =(h-40) * 1.5*r
total += 40 * r
print(total)