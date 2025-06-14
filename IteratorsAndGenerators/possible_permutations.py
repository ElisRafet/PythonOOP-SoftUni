def possible_permutations(ls):
    if len(ls) <= 1:
        yield ls

    else:
        for i in range(len(ls)):
            curr_el = ls[i]
            remaining_els = ls[:i] + ls[i + 1:]
            permutations = possible_permutations(remaining_els)
            for permutation in permutations:
                yield [curr_el, *permutation]