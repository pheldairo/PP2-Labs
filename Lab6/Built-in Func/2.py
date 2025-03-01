string = input()
print(f'sum of upper case: {len([i for i in string if i.isupper()])}')
print(f'sum of lower case: {len([i for i in string if i.islower()])}')