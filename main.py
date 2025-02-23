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