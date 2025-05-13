# collections: OrderedDict.
# dict subclass that remembers the order entries were added


from collections import OrderedDict

ordered_dict = OrderedDict()

ordered_dict["b"] = 2
ordered_dict["c"] = 3
ordered_dict["d"] = 4
ordered_dict["e"] = 5
ordered_dict["f"] = 6
ordered_dict["g"] = 7
ordered_dict["a"] = 1


print(ordered_dict)