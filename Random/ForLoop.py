def loop(n):
    for i in range(n):
        print(i, end=" ")
        for j in range(i):
            print(j, end=" ")
            for k in range(j):
                print(k, end=" ")
        print()


loop(7)
