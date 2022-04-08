def pall(str):
    if str[::-1] == str:
        return "It is a Pallindrome"
    else:
        return "It is not a Pallindrome"


print(pall("aram"))
