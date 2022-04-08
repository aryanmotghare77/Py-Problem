def dupli(items):
    n = 0
    d = items[n]
    for x in items:
        if x == d:
            print("Duplicate Available")
        else:
            print("Duplicate not Available")
        n += 1


dupli([1, 2, 21, 3, 32])
