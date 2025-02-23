import re
test_string = "a1B2c3D4"
answer = re.split(r'[A-Z]', test_string)
print(answer)