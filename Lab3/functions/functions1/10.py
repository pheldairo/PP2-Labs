def unique(input_list):
    unique_list = []
    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

testList = list(input("Enter a list: "))
print(unique(testList))  