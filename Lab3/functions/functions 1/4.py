def isPrime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if isPrime(num)]

numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
prime_numbers = filter_prime(numbers)
print("Prime numbers:", prime_numbers)