import pickle
import requests
import pandas as pd
import numpy as np

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))
#movie='Batman'

def ind(movie):
    i = movies[movies['title'] == movie].index[0]
    return(i)

def get_movie_names():
    return movies['title'].values

def fetch_poster(movie_id):
   response =  requests.get('https://api.themoviedb.org/3/movie/{}?api_key=6810f42be45a708384f75bec6cac4f0c&language=en-US'.format(movie_id))
   data = response.json()
   return "https://image.tmdb.org/t/p/w500/"+data['poster_path']

def fetch_overview(movie_id):
   response =  requests.get('https://api.themoviedb.org/3/movie/{}?api_key=6810f42be45a708384f75bec6cac4f0c&language=en-US'.format(movie_id))
   data = response.json()
   return data['overview']

def recommend(movie):
    
    movie = movie.strip()
    print(movie)
    index = ind(movie)
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    recommended_movies = []
    recommended_movies_posters= []
    for i in distances[1:7]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))     
  
    return (recommended_movies)

def recommend_poster(movie):
    index = ind(movie)
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    recommended_movies = []
    recommended_movies_posters= []
    for i in distances[1:7]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))     
  
    return (recommended_movies_posters)

def recommend_overview(movie):
    index = ind(movie)
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    recommended_movies = []
    recommended_movies_overview= []
    for i in distances[1:7]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_overview.append(fetch_overview(movie_id))     
  
    return (recommended_movies_overview)




if __name__ == '__main__':

    #print(get_movie_names())
    #print(recommend('Avatar'))
    #print(fetch_poster(65))
    print(recommend_poster('Avatar')[0])