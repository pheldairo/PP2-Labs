import re

pattern = r"[A-Z][a-z]+"
answer = "Hello world! This Is a Test String with MixedCase and lowercase."
print(re.findall(pattern, answer))