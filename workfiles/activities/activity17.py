def act17():
    print("------------------- < Loops > -------------------\n")
    columns = eval(input("Enter number of Columns : "))

    for x in range(1,11): 
        for y in range(1, columns + 1):
            print(f"{x} x {y} = {x * y}", end ="\t")
        print()