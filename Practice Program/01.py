sum = 0
while True:
    inp = input("Enter the Number :  ")
    if inp != "q":
        sum = sum + int(inp)
        print("Enter q to Exit")
        print(f"{n}. {inp}")
        n += 1
    else:
        print(f"The Bill Total is {sum}")
        print("Thanx for Using the Calculator")
        break
