from helper import d

# Immuability means data of a tuple cannott be adjusted in iits location in memory

tup1 = (1,2,3,4,5)
print(tup1)

# tup1[3] = 'four' # throws a type error since tuples cant do this, lists can though!

# YOU CANNT CHANGE TUPLE DATA IN PLACE

d()

# samll workaround to change items in a tuple 
# we can type cast the tuple into a list, make our changes, convert it back to a tuple
print(id(tup1))
tup1 = list(tup1) # type cast into a list 
tup1[3] = 'four' # CHANGE SOME DATA 
tup1 = tuple(tup1) # Type cast back into a tuple
print(id(tup1))

print(tup1)

d()

#--- concatenating tuples : adding them together 

tup1 = 1,2,3,4,5
tup2 = 6,7,8,9,10
tup1 += tup2
print(tup1)

#-- repeating tuples

short_story = 'A Tale',
print(short_story)
anothology = short_story * 3
print(anothology)



