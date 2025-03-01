for i in range(ord('A'), ord('Z') + 1):
    with open(f"{chr(i)}.txt", 'x'):
        print(f"{chr(i)}.txt was created")