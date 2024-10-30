def is_prime(func):
    def wrapper(*args):
        result_func = func(*args)
        if result_func == 2:
            print(f'Простое')
        elif result_func % 2:
            print(f'Простое')
        else:
            print(f'Составное')
        return result_func

    return wrapper


@is_prime
def sum_three(a, b, c):
    return sum([a, b, c])


result = sum_three(2, 3, 6)
print(result)

