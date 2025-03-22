## David Nguyen
## Learn basic Python Basic Syntax
## Basic of Python
### Containers
#### Lists
xs = [3, 2, 1]  #create list
print(xs)
print(xs[0])  #access list
print(xs, xs[1])  #access last element
print(xs[-1])  # negative indices count form the end of the list; prints "2"
xs[2] = 'foo'  # lists can cointain different types
print(xs)
#add a new element to the end of the list
xs.append('bar')
print(xs)
#Remove and return the last element of the list
x = xs.pop()
print(x, xs)
#### Slicing
# in addition to access list elements, you can also access a slice of the list. Python provides consise syntax to access sublists. this know as slicing.
#range is a built-in function that returns a list of integer
nums = range(5)
print(nums)
print(nums[2:4])  #get a slice from index 2 to 4 (exclusive)
print(nums[2:])  #get a slice from index 2 to the end
print(nums[:2])  #get a slice from the start to index 2 (exclusive)
print(list(nums))
print(list(nums)[2:4])
print(list(nums)[2:])
print(list(nums)[:2])
print(list(nums)[:])
print(list(nums)[:-1])  #every other element
print(list(nums)[1::2])  #every other element starting at index 1
print(list(nums)[::2])  #every other element starting at index 0
#Assign a new sublist to a slice
new_nums = [i for i in nums]
print(new_nums)
new_nums[2:4] = [8, 9]
print(new_nums)
#### Loops
animals = ['cat', 'dog', 'monkey']
for animal in animals:
  print(animal)
for idx, animal in enumerate(animals):
  print('#%d: %s' % (idx + 1, animal))
  #### List comprehensions:
  ## When programming, frequently we want to transform one type of data into another. As a simple example, consider the following code that computes square numbers:
  nums = [0,1,2,3,4]
  print(nums)
  squares = []
  for x in nums:
    squares.append(x**2)
print(squares)
### make this code simpler using a list comprehension:
nums = [0,2,3,4,5]
squares = [x**2 for x in nums]
print(squares)
## list conprehensions can also contain conditions:
nums = [0,1,2,3,4]
even_squares = [x**2 for x in nums if x%2 ==0]
print(even_squares)
##### Dictionaries
## A dictionary stores (key, value) pairs, similar to a `Map` in Java or an object in Javascript. You can use it like this:
d = {'cat':'cute', 'dog':'furry'}
print(d['cat']) #Get an entry from a dictionary; prints "cute"
print('cat' in d) #Check if a dictionay has a given key; print "True"
d['fish'] = 'wet' #set an entry in dictionary
print(d['fish'])
# Get an element with a default; prints "N/A"
#print(d['monkey'])
print(d.get('monkey', 'N/A')) # "fish" is no longer a key; prints "N/A"
#It is easy to iterate over the keys in a dictionary:
d = {'person':2, 'cat':4, 'spider':8}
for animal in d:
  legs = d[animal]
  print('A %s has %d legs' % (animal, legs))
#If you want access to keys and their corresponding values, use the iteritems method:
#dict.iteritems() will in Python 3
for animal, legs in d.items():
  print('A %s has %d legs' % (animal, legs))

#Dictionary comprehensions: These are similar to list comprehensions, but allow you to easily construct dictionaries. For example:
nums = [0,1,2,3,4]
even_num_to_square = {x:x **2 for x in nums if x%2 ==0}
print(even_num_to_square)
