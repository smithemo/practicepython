#Program takes a list and removes duplicates
#Goal is to use 2 methods - list manipulation and Sets

from random import randint

#creates a random list of integers of a random size
a = [randint(1,21) for x in range(randint(5,26))]

def unique1(mylist):
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    return b

def unique2(mylist):
    return(set(a))

print (a)
print(sorted(unique1(a)))
print(unique2(a))
