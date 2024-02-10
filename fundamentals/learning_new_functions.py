'''
reverse function: traverse in reverse without using indexes
'''
l = [1,2,3,4,5]
for n in reversed(l): print(n)
print("\n---------------------------\n")


'''
yield function
'''
def generator_function():
    yield 'first-val'
    yield 'second-val'
    yield 'third-val'
    yield 4

my_generator = generator_function()
for val in my_generator: print(val)
print("\n---------------------------\n")




'''
itertools.izip_longest
'''
import itertools

itr1 = [1,2,3]
itr2 = ['a','b']
itr3 = ['FIRST']

for item in itertools.zip_longest(itr1, itr2, itr3, fillvalue=None): print(item)
print("\n---------------------------\n")
