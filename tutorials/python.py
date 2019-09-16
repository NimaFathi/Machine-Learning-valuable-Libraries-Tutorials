animals = ['cat', 'dog', 'monkey']
for id, animal in enumerate(animals):
    print('#%d: %s' % (id + 1, animal))
nums = [1,2,3]
squares = [x ** 2 for x in nums if x <3]
print(squares)


dic = {'monkey': 'mon', 'fish': 'fi', 'cat': 'ca'}
print(dic.get('monkey', 'N/A'))
print(dic.get('dog', 'N/A'))

d = {'person': 2, 'cat': 4, 'spider': 8}
for animal, legs in d.items():
    print('A %s has %d legs' % (animal, legs))
# Prints "A person has 2 legs", "A cat has 4 legs", "A spider has 8 legs"

d = {(x, x + 1): x for x in range(10)}  # Create a dictionary with tuple keys,(x, x+1) as key and x as value
t = (5, 6)        # Create a tuple
print(type(t))    # Prints "<class 'tuple'>"
print(d[t])       # Prints "5"
print(d[(1, 2)])  # Prints "1"


