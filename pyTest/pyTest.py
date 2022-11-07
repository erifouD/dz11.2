n = int(input())
if n < 4:
    print("0")
else:
    if n % 2 == 0:
        print(n - 2, "\n", int(n / 2), " ", int(n / 2 + 2))
    else:
        print(n - 3)
    for i in range (n - 3):
        print(1, " ", i + 3)