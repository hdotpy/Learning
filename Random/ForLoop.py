def loop(n):
    for i in range(n):
        print(i, end=" ")
        for j in range(n):
            print(j, end=" ")
        print()


loop(7)
