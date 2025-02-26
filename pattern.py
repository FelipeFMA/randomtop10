def pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))

size = int(input("Enter the size of the pyramid: "))

if size <= 1:
    print("It must be at least 2.")
else:
    pyramid(size)

