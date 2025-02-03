def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print(f"Prime numbers in the list: {prime_numbers}")