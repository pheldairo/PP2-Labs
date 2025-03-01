data = []
for i in input().split():
    data.append(True) if i == "y" else data.append(False)
print(all(tuple(data)))