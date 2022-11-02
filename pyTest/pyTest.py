count = int(input("Count of numbers: "))
Arr = []
Daymar = []
Aberdeen = []
for i in range(count):
    Arr.append(int(input("Number: "))) 

max = Arr[0]
min = Arr[0]
for i in range(count):
    if Arr[i] > max:
        max = Arr[i]

    if Arr[i] < min:
        min = Arr[i]

    if int(Arr[i]) % 2 == 0:
        Daymar.append(Arr[i])

for i in range(len(Daymar)):
    temp = str(Daymar[i])
    tempsum = 0
    for i in range(len(temp)):
        tosum = int(temp[i])
        tempsum = tempsum + tosum
    Aberdeen.append(tempsum)

print("\nLargest number: ", max, "\nSmallest number: ", min)

for i in range(len(Daymar)):
    print("\nHonest number #", i + 1, ": ", Daymar[i], " Digits sum: ", Aberdeen[i], "  Degree: ", Daymar[i] ** Daymar[i])