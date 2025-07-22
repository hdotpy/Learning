def pyramid(count):

    for i in range(count):
        print(" " * (count-i-1), end="")
        for j in range(1, 2*i+2):
            print("*", end="")
        print()
    for i in range(count, 0, -1):
        print(" " * (count-i), end="")
        for j in range(2*i-1):
            print("*", end="")
        print()


n = int(input("Enter the number of rows for the pyramid: "))
pyramid(n)
