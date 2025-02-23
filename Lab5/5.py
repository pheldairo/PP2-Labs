import re

answer = "a123b aAb a1b a_b a!b aZb"
print(re.findall(r"a[a-zA-Z\d]*b", answer))