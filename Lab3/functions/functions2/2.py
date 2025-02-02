from folder.dictionary import movies

def list_imdb(list):
    return [i for i in list if i['imdb'] > 5.5]

print(*list_imdb(movies))