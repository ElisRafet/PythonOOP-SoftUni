def get_primes(numbers):
    for num in numbers:
        if num < 2:
            continue
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            yield num