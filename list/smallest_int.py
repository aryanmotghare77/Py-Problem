def smallest(items):
    min = items[0]
    for a in items:
        if a < min:
            min = a

    return min


print(smallest([2, 3, 1, 23, 34, 11]))
