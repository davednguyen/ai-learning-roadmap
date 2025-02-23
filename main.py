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