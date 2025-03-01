data = [i for i in input().split()]
with open("text.txt", 'a') as file:
    file.write(f"\n{str(data)}\n")