class MySet:
    def __init__(self, enumerable=[]):
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True

    def has(self, value):
        return value in self.dictionary

    def add(self, value):
        self.dictionary[value] = True
        return self

    def delete(self, value):
        self.dictionary.pop(value, None)
        return self

    def size(self):
        return len(self.dictionary)

    def clear(self):
        self.dictionary.clear()

    def __str__(self):
        set_list = []
        for key, value in self.dictionary.items():
            set_list.append(str(key))
        return f'MySet: {{{",".join(set_list)}}}'
my_set = MySet([1, 2, 3, 3])

print(my_set.has(2))  # True
print(my_set.has(4))  # False

my_set.add(4)
print(my_set)  # MySet: {1,2,3,4}

my_set.delete(3)
print(my_set)  # MySet: {1,2,4}

print(my_set.size())  # 3

my_set.clear()
print(my_set)  # MySet: {}

