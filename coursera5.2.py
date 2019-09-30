largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        temp = int(num)
        if largest==None or largest<temp:
            largest = temp
        if smallest==None or smallest>temp:
            smallest = temp
    except:
        print("Invalid input")
    

print("Maximum is",largest)
print("Minimum is",smallest)