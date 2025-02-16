n = int(input())
even_nums = (str(i) for i in range(n + 1) if i % 2 == 0)
print(", ".join(even_nums))
