from folder.dictionary import movies

def filter_by_category(list : list, category : str):
    return [i for i in list if i['category'] == category]

print(filter_by_category(list = movies, category = input()))