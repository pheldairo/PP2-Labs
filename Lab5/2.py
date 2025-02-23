import re

content = "aabbb abbb aaabbb aaaaabbb bbb aabbbb"

pattern = r'a+bbb'

print(re.findall(pattern, content))