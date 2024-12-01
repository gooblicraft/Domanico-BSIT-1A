num = eval(input("Please input the number of your triangles : "))

for repeat in range(0, num+1):
    for x in range(1, 7):
        for a in range(1, x+1):
            print("*", end =" ")
        for b in range(7, x-1, -1):
            print(" ", end=" ")
        print()
    print(end=" ")