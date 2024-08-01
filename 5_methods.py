from helper import d 

# Tuple methods

# tuples don't have any methods of their own 

#-- tuple.count(item) : counts how many times an item appears in a tuple

shopping = 'eggs', 'milk', 'creamer', 'creamer', 'creamer', 'chicken'

print(shopping.count('creamer'))
print(shopping.count('chicken'))

d()

#-- len(tuple) : returns the length of the given item 

print(len(shopping))

#-- tuple.index(item) : returns the index of that item

print(shopping.index('creamer'))
print(shopping.index('chicken'))

#-- membership checks of a tuple, if item in tuple, 'in', return True or False 

print('creamer' in shopping)
print(' Cinnamon toast crunch' in shopping) 

nest = 'start', ('early', 'middle', 'towards end'), 'end'

for item in nest:
    if isinstance(item, tuple) and 'middle' in item:
        print('I found the middle!!')