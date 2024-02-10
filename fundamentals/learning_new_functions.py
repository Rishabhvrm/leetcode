'''
reverse function: traverse in reverse without using indexes
'''
print("\n---------------------------\nreversed():")
l = [1,2,3,4,5]
for n in reversed(l): print(n)



'''
yield function
'''
def generator_function():
    yield 'first-val'
    yield 'second-val'
    yield 'third-val'
    yield 4

print("\n---------------------------\nyield:")
my_generator = generator_function()
for val in my_generator: print(val)



'''
zip function
'''
print("\n---------------------------\nzip():")
z1, z2 = [1,2,3,4], ["FIRST", "SECOND", "THIRD"]
for ele in zip(z1,z2): print(ele)   # notice, missing '4' in the output



'''
itertools.zip_longest
'''
print("\n---------------------------\nzip_longest():")
import itertools

itr1 = [1,2,3]
itr2 = ['a','b']
itr3 = ['FIRST']

for item in itertools.zip_longest(itr1, itr2, itr3, fillvalue=None): print(item)
