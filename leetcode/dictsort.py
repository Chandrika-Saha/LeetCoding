d = {"c":3, "a":1, "b":2}
print("Unsorted dict: ", d)

# Sort by keys
d = dict(sorted(d.items()))
print("Sorted by keys: ", d)

d = {"apple":5, "banana":2, "pear":7, "orange":3}
print("Unsorted dict: ", d)

# Sort by Values
da = dict(sorted(d.items(), key=lambda x: x[1]))
print("Sorted by values (ascending): ", da)

dd = dict(sorted(d.items(), key=lambda x:x[1], reverse=True))
print("Sorted by values (descending): ", dd)

d = {"a":3, "c":1, "b":1, "d":3}
print("Unsorted dict: ", d)

# Sort by value and then by key
d = dict(sorted(d.items(), key=lambda x:(x[1], x[0])))
print("Sorted by value and then by key: ", d)

d = {"a":10, "b":5, "c":20, "d":15}
k = 2
print("Unsorted dict: ", d, " and the k for the top k: ", k)

# The top k keys with the highest values
d = dict(sorted(d.items(), key=lambda x:x[1], reverse=True))
print(f"The top {k} with the highest values are: {list(d.keys())[:k]}")


