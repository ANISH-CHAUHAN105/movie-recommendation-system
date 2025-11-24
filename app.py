import streamlit as st
import pickle
import pandas as pd
import requests

st.header("Movie Recommender System")

movies = pd.read_pickle("movie_list.pkl")
similarity = pickle.load(open("similarity.pkl", "rb"))

TMDB_API_KEY = 32d521970ff7efd2cfdb42bb8b96b2e7

def fetch_poster(movie_title):
    url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={movie_title}"
    response = requests.get(url).json()

    if response["results"]:
        poster_path = response["results"][0].get("poster_path")
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500{poster_path}"

    return "https://via.placeholder.com/500x750?text=No+Image"

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    sorted_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_titles = []
    recommended_posters = []

    for i in sorted_list:
        title = movies.iloc[i[0]].title
        recommended_titles.append(title)
        recommended_posters.append(fetch_poster(title))
    
    return recommended_titles, recommended_posters


movie_list = movies['title'].values
selected_movie = st.selectbox("Select or search a movie", movie_list)

if st.button("Recommend"):
    names, posters = recommend(selected_movie)

    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])
