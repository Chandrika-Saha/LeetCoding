class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.count = 0
        # table = [ [], [] ]

    def _hash(self, key):
        # 100, 200
        return hash(key) % self.size

    def put(self, key, value):
        index = self._hash(key)

        # update if key exists
        # [[val1, val2]]
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return

        # otherwise insert
        self.table[index].append((key, value))
        self.count += 1

    def get(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        raise KeyError(key)

    def remove(self, key):
        index = self._hash(key)
        for i, (k, _) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                self.count -= 1
                return
        raise KeyError(key)

    def contains(self, key):
        index = self._hash(key)
        return any(k == key for k, _ in self.table[index])

    def keys(self):
        return [k for bucket in self.table for k, _ in bucket]

    def values(self):
        return [v for bucket in self.table for _, v in bucket]

    def items(self):
        return [(k, v) for bucket in self.table for k, v in bucket]

    def __len__(self):
        return self.count

    def __str__(self):
        return "{" + ", ".join(f"{k}: {v}" for k, v in self.items()) + "}"

ht = HashTable()

ht.put("apple", 5)
ht.put("banana", 3)
ht.put("orange", 10)

print(ht.contains("apple"))   # True
print(ht.contains("grape"))   # False

print(ht.keys())              # ['apple', 'banana', 'orange']
print(ht.values())            # [5, 3, 10]
print(ht.items())             # [('apple', 5), ('banana', 3), ('orange', 10)]

print(len(ht))                # 3
print(ht)                     # {apple: 5, banana: 3, orange: 10}
