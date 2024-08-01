from helper import d

# unpacking Tuples 

# reminder 
packed = 'bacon', 'lettuce', 'tomato'
print(packed)

# basic unpacking

first, second, third = packed
print(first)
print(second)
print(third)

# will trhow ValueError if the variables and items are not equal in number
#-- too many values to unpack, not enough variables 
#-- too many Variables, not enough data to unpack into them 
d()

# Extended unpacking : *var takes any additional data and packs it into a list

enhanced_blt = 'bacon', 'lettuce', 'tomato', 'mayo', 'avocado', 'everything bagel seasoning'
print(enhanced_blt)

d() 

first, second, third, *condiments = enhanced_blt
print(first)
print(second)
print(third)
print(condiments)
d()

story = 'intro', 'conflict', 'buildup', 'big reveal', 'climax', 'conclusion'
beging, fight, *middle, end = story 
print(beging)
print(fight)
print(tuple(middle))
print(end)

# you cannot have multiple * expresions or youll get a SyntaxError