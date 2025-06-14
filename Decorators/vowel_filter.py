def vowel_filter(function):
    def wrapper():
        result = function()
        return [c for c in result if c in "aeuio"]
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())