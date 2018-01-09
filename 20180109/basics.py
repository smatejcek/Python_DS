#1 Lists
# Ordered
# Mutable

from functools import reduce

odds = [5, 7, 9]
total = 0

for i, num in enumerate(odds):
    total += num * i

#list comprehenson
squareroots = [n**2 for n in odds]
cuberoots = [n**(1 / 3) for n in odds]
divisibleby5 = [n**(1 / 3) for n in range(31) if n%5 == 0]

list(map(lambda n: n**(1 / 3), odds))

list(filter(lambda n: n < 5, [3, 4, 5, 6, 7]))

reduce(lambda total, n: total + n, odds, 0) # Zero initializes total


# Tuples
# Ordered
# Immutable

tup1 = (3, 4)

#Sets
#No Order, but iterable
#Unique values
#Immutable

set1 = {1, 2, 3}
set2 = {3, 4, 5}

set1 & set2 #Intersection, 3
set1 | set2 # Union 1, 2, 3, 4, 5
set1 ^ set2 #Disunion 1, 2, 4, 5, what they don't have in comon


#Dictionaries
#No Order
#Keys must be unique and hashable
