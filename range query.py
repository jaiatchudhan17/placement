i, j = map(int, input("ENTER A NUMBER: ").split())

if 0 <= i < j <= 9999:
    total = 0
    for num in range(i, j + 1):
        total += num
    print(total)
else:
        print("Invalid Input")
