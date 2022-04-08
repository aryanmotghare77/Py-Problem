def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n - 1)


def factZero(n):
    i = 5
    count = 0
    while n // i != 0:
        count += int(n / i)
        i = i * 5
    return count


inp = int(input("Enter the Number : "))
print(fact(inp))
print(factZero(inp))
