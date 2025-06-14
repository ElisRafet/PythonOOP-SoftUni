def type_check(type):
    def decorator(function):
        def wrapper(par):
            if isinstance(par, type):
                result = function(par)
                return result
            else:
                return "Bad Type"
        return wrapper
    return decorator



@type_check(int)
def times2(num):
    return num*2

print(times2(2))
print(times2('Not A Number'))