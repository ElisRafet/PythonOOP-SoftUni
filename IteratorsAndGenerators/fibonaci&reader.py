# def fibonacci():
#     first_num, next_num = 0, 1
#     while True:
#         yield first_num
#         first_num, next_num = next_num, first_num + next_num

# generator = fibonacci()
# for i in range(5):
#     print(next(generator))

def read_next(*args):
    for arg in args:
        yield from arg


# for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
#     print(item, end='')