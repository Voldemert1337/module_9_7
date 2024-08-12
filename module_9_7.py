def is_prime(func):
    def wrapper(*args):
        add = func(*args)
        count = 0
        for i in range(1, add + 1):
            if add % i == 0:
                count += 1
        return f'Простое \n{add}' if count == 2 else f'Составное \n{add}'

    return wrapper




@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(1, 32, 3)
print(result)