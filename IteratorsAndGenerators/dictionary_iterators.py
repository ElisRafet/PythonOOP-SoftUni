class dictionary_iter:
    def __init__(self, data: dict):
        self.data_tuple = tuple(data.items())
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self.data_tuple):
            raise StopIteration
        return self.data_tuple[self.index]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)