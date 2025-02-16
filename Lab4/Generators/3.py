def divisible_by_3_and_4(n):
    return (i for i in range(n + 1) if i % 3 == 0 and i % 4 == 0)

n = 50
for number in divisible_by_3_and_4(n):
    print(number)
