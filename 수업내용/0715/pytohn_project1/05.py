import json
from pprint import pprint


def genres_info(movies, genres) :
    genres_name = []
    for genres in genres_list :
        
        for movie_g in movies['genre_ids'] :
            if genres['id'] == movie_g :
                genres_name.append(genres['name'])
    return genres_name

def movie_info(movie, genres_list):
    return {'genre_name' : genres_info(movie, genres_list),
            'id' : movie['id'],
            'overview' : movie['overview'],
            'title' : movie['title'],
            'vote_average' : movie['vote_average']}
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))