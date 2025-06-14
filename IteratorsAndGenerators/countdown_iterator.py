class countdown_iterator:
    def __init__(self, count):
        self.count = count

    def __iter__(self):
        return self
    def __next__(self):
        num = self.count
        self.count -= 1
        if self.count < -1:
            raise StopIteration
        return num

iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")