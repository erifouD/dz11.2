count = int(input("Count of numbers: "))
Arr = []
for i in range(count):
    Arr.append(int(input("Number: "))) 
print("\nLargest number: ", max(Arr), "\nSmallest number: ", min(Arr))
for i in range(count):
    if int(Arr[i]) % 2 == 0:
        temp = str(Arr[i])
        tempsum = 0
        for j in range(len(temp)):
            tosum = int(temp[j])
            tempsum = tempsum + tosum
        print("Honest number: ", Arr[i], "  Digits sum: ", tempsum, "Degree: ", tempsum ** tempsum)