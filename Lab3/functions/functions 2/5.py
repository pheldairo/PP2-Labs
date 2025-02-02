from folder.dictionary import movies

def averageCategory(list, category):
    sum , count = 0, 0
    for i in list:
        if i['category'] == category:
            sum += i["imdb"]
            count += 1
    try:
        return sum / count
    except ZeroDivisionError:
        return "Category not found, try again."
    
print(averageCategory(movies, input()))