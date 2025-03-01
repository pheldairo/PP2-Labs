string = input()

string2 = ''
for i in reversed(string):
    string2+=i

print(string == string2 and string == string[::-1])