def largest_int(items):
    max = items[0]
    for x in items:
        if x > max:
            max = x
    return max


print(largest_int([12, 23, 2, 21, 1]))
