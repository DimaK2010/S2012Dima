#1 - iterators
           #0 1 2 3 4
lessons = [1, 2, 3, 4, "Test5", 8, 10, 22, ]
iterator = iter(lessons)
#print(iterator)
...
try:
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
except StopIteration:
    print("StopIteration")
...
try:
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
except StopIteration:
    print("StopIteration")
...
print(next(iterator))
print(next(iterator))
print(next(iterator))
for elem in iterator
    print(f"from for: {elem}")
    print(next(lessons))
except TypeError as te:
print(te)
[9:07] Андрій Применко

#2 - counter
from counter import Counter
counter = Counter(13)

'''
for number in counter:
    print(number)
'''
while(True):
    try:
        print(next(counter))
    except StopIteration:
        break
