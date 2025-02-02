from folder.dictionary import movies

def average_imdb(list):
    sum = 0
    for i in list:
        sum += i['imdb']
    avg = sum / len(list)
    print(round(avg, 1))
    
average_imdb(movies)