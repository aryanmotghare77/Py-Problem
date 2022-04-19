def int_sum(n1,n2,n3):
    if(n1==n2 or n1==n3 or n2==n3):
        return 0
    else:
        return n1+n2+n3

print(int_sum(1,3,32))