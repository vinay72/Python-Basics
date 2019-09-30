def computepay(h,r):
    total=40*r
    if(h>40):
        total += (h-40)*r*1.5
    return total

hrs = int(input("Enter Hours:"))
rate = float(input("Enter rate:"))
print(computepay(hrs,rate))