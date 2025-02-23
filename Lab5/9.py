import re
test_string = 'Hello World This Is A Test String with MixedCASE'
upper_words = re.findall(r"[A-Z][a-z]+", test_string)
print(*upper_words)