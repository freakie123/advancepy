
numbers = [1,56,234,87,4,76,24,69,90,135]

def is_even(r):
    return r %2==0 

#even numbers with filter
print(list(filter(is_even, numbers)))

print ( list ( filter(lambda r: r % 2 == 0, numbers)))


#odd Numbers with filter
def odd(r):
    if not r%2 ==0:
        return True
    else:
        return False
#    return r%2 != 0

print(list(filter(odd, numbers)))
