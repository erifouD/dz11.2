count = int(input("Count of numbers: "))
Arr = []
Daymar = []
Aberdeen = []
for i in range(count):
    Arr.append(int(input("Number: "))) 
for i in range(count):
    if int(Arr[i]) % 2 == 0:
        Daymar.append(Arr[i])
print("\nLargest number: ", max(Arr), "\nSmallest number: ", min(Arr))
for i in range(len(Daymar)):
    temp = str(Daymar[i])
    tempsum = 0
    for i in range(len(temp)):
        tosum = int(temp[i])
        tempsum = tempsum + tosum
    Aberdeen.append(tempsum)
for i in range(len(Daymar)):
    print("\nHonest number #", i + 1, ": ", Daymar[i], " Digits sum: ", Aberdeen[i], "  Degree: ", Daymar[i] ** Daymar[i])