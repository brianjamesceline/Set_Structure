# Set items are enclosed in curly brackets
# Set is unordered
# Set is mutable
# Set elements are unique
# Elements can contain only immutable items



'''
Python Set Attributes
'''

# print(dir(set))

'''
Creating Python Sets
'''

# set = set()
# set = {1,2,3}
# print(set)

'''
Modifying a Set in Python
'''

# set_example = {'hello', 'world'}
# # set_example[0]
# set_example.add('yay')
# set_example.add('hey')
# set_example.update([1,2,3])

# print(help(set.update))
# print(set_example)

'''
Removing Elements from a Set
'''

# set_example = {1,2,3,4,5,6,7,8}

# set_example.discard(1)
# set_example.remove(1)
# set_example.pop()
# print(set_example)
# print({'hello', 'world', 'hello', 'hello'})


'''
Set Union Operations
'''

# a = {1,2,3,6,7}
# b = {4,5,6,7,8,9}

# print(a | b)
# print(a.union(b))

'''
Set Intersection Operations
'''

# a = {1,2,3,6,7}
# b = {4,5,6,7,8,9}

# print(a & b)
# print(a.intersection(b))


'''
Set Difference Operations
'''

# a = {1,2,3,4,6,7,9}
# b = {2,5,6,7,8,9}

# print(a - b)
# print(b - a)
# print(a.difference(b))
# print(b.difference(a))

'''
Set Symmetric Difference
'''

# a = {1,2,3,4,6,7,9}
# b = {2,5,6,7,8,9}

# print(a ^ b)
# print(a.symmetric_difference(b))

'''
Set Methods
'''

print(dir(set))