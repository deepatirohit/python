# collections: defaultDict

# It automatically assigns a default value to a key if the key is not present.

from collections import defaultdict

d = defaultdict(int)
d["a"] = 1
d["b"] = 2

print(d)
print(d["a"])
print(d["b"])
print(d["c"]) #this will return zero