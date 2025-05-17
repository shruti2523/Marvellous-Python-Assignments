from MarvellousNum import ChkPrime

def ListPrime(lst):
    return sum([x for x in lst if ChkPrime(x)])

lst = [13, 5, 45, 7, 4, 56, 10, 34, 2, 5, 8]
print("Output:", ListPrime(lst))
