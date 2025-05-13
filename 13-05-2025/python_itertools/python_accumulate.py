from itertools import accumulate
import operator

a = [1, 2, 3, 4]
acc = accumulate(a)

print(a)

print(list(acc))

a = [1, 2, 3, 4]
acc = accumulate(a, func=operator.mul)
print(list(acc))


a = [1, 2,7, 3, 4]
acc = accumulate(a, func=max)
print(list(acc))