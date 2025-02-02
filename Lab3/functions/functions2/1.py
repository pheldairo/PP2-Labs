from folder.dictionary import movies

def is_high_score(movie):
    return movie.get('imdb', 0) > 5.5

print(is_high_score(movies[0]))
