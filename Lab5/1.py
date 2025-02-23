import re

content = "aaabbb aab ab aaaaabbbb bbaaa"

pattern = r'a*b*'
matches = re.findall(pattern, content)

print(matches)