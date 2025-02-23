import re

answer = "Hello, world. This is a test string"
print(re.sub(r"[ ,.]", ':', answer))