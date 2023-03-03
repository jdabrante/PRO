def evens(lim):
    for i in range (0, lim + 1,2):
        yield i 

evens_gen = evens(50)

for even in evens_gen: 
    print(even, end=" ")