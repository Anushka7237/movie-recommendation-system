import streamlit as st
import pickle
import pandas as pd
import numpy as np
from config import API_KEY
import requests
import time

PLACEHOLDER_POSTER = "https://via.placeholder.com/300x450?text=No+Poster"

def fetch_posters(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {
        "api_key": API_KEY,
        "language": "en-US"
    }

    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()

        poster_path = data.get("poster_path")
        if poster_path:
            return "https://image.tmdb.org/t/p/w500" + poster_path
        else:
            return PLACEHOLDER_POSTER

    except requests.exceptions.RequestException as e:
        print(f"TMDB request failed for movie_id {movie_id}: {e}")
        return PLACEHOLDER_POSTER


movies_dict=pickle.load(open("movies_dict.pkl","rb"))
similarity=pickle.load(open("similarity.pkl","rb"))
movies=pd.DataFrame(movies_dict)

def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommend_movies=[]
    recommend_posters=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].id
        recommend_movies.append(movies.iloc[i[0]].title)
        recommend_posters.append(fetch_posters(movie_id))
        time.sleep(0.2)
    return recommend_movies,recommend_posters
        
     
st.title("🎬 Movie Recommender System")

selected_movies_names=st.selectbox(
    'Which type of movie do you want to be recommended!!',
    movies['title']
)

if st.button("Recommend"):
    with st.spinner("Finding great movies for you..."):
        names, posters = recommend(selected_movies_names)
        
    if len(names) == 0:
        st.warning("No recommendations found.")
    else:
        cols = st.columns(len(names))
        for i in range(len(names)):
            with cols[i]:
                st.text(names[i])
                st.image(posters[i])

    

        
        
        
        
        
        
        
       