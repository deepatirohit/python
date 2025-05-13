# collections: deque
# It’s like a list, but optimized for fast appends and pops from both ends (O(1) time complexity

from collections import deque
d = deque()

d.append(1)
d.append(2)

print(d)

d.appendleft(0)
print(d)

d.append(3)
print(d)

print(d.pop())
print(d.popleft())

print(d)

# print(d.clear())

d.extend([4,5,6,7])
print(d)

d.extendleft([-3, -2, -1, 0])
print(d)

