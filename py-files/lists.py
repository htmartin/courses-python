#!/usr/bin/python

q='dogs are puppies at one point I believe'.split()
t='1/2/3/4/5/6/7/8'.split('/')
y=[1,2,3,4,5,6,7,8]
a=[3, 2, 4, 6, 7, 9, 1, 5, 8]
v=set([3, 2, 4, 6, 7, 9, 1, 5, 8])

print(q[4])

print(i=q.index('puppies'))

print()
print(del q[5])

print(q.insert(5, 'point'))

print(q.remove('puppies'))
print(del q[q.index('believe')])
print(q.insert(-1, 'believe'))

To return a new list which is a sorted version of an existing list:
m=sorted(q)
n=reversed(q)
o=q[::-1]

y=[1,2,3,4,5,6,7,8]
>>> y[::-1]
[8, 7, 6, 5, 4, 3, 2, 1]
>>> sorted(y)
[1, 2, 3, 4, 5, 6, 7, 8]
>>> sorted(y, reverse=True)
[8, 7, 6, 5, 4, 3, 2, 1]

For the reverse iterator:
>>> p=[9,3,1,0]
>>> e=reversed(p)
>>> e
<list_reverseiterator object at 0x10c62a4a8>
>>> list(e)
[0, 1, 3, 9]

Ordering sorted sets:
>>> q='dogs are puppies at one point I believe'.split()
>>> q
['dogs', 'are', 'puppies', 'at', 'one', 'point', 'I', 'believe']
>>> set(q)
{'point', 'dogs', 'one', 'are', 'at', 'puppies', 'I', 'believe'}
>>> q
['dogs', 'are', 'puppies', 'at', 'one', 'point', 'I', 'believe']
>>> s=set(q)
>>> s
{'point', 'dogs', 'one', 'are', 'at', 'puppies', 'I', 'believe'}
>>> sorted(s)
['I', 'are', 'at', 'believe', 'dogs', 'one', 'point', 'puppies']
>>> sorted(s)[0:2]
['I', 'are']


>>> v=set([3, 2, 4, 6, 7, 9, 1, 5, 8])
>>> v
{1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> sorted(v)
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> sorted(v,reverse = True)
[9, 8, 7, 6, 5, 4, 3, 2, 1]



To sort list in place (in situ):
>>> r=q.sort()
>>> r
>>> q
['I', 'are', 'at', 'believe', 'dogs', 'one', 'point', 'puppies']

>>> q="the rabbit eats carrots".split()
>>> q
['the', 'rabbit', 'eats', 'carrots']
>>> q.reverse()
>>> q
['carrots', 'eats', 'rabbit', 'the']


>>> q.sort(key=len)
>>> q
['I', 'at', 'are', 'one', 'dogs', 'point', 'puppies', 'believe']

>>> ' '.join(q)
'I at are one dogs point puppies believe'
>>> q
['I', 'at', 'are', 'one', 'dogs', 'point', 'puppies', 'believe']

