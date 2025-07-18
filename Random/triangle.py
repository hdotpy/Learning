row = 7
for i in range(row):
    for j in range(row):
        if i == j or j == row - i - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
