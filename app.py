import streamlit as st
import pandas as pd
import pickle

movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

title_to_index = pd.Series(movies.index, index=movies['title'].str.lower()).to_dict()

def recommend(movie_title):
    movie_title = movie_title.lower().strip()
    
    if movie_title not in title_to_index:
        return []

    idx = title_to_index[movie_title]
    distances = similarity[idx]

    similar_indices = distances.argsort()[-6:-1][::-1]

    return movies.iloc[similar_indices]['title'].tolist()

st.title("🎬 Simple Movie Recommendation System")

movie_name = st.text_input("Enter a movie name:")

if st.button("Recommend"):
    if movie_name.strip() == "":
        st.warning("Please enter a movie name.")
    else:
        results = recommend(movie_name)
        if not results:
            st.error("Movie not found in the dataset.")
        else:
            st.subheader("Recommended Movies:")
            for m in results:
                st.write("• " + m)

st.write("---")
st.caption("Built with Streamlit")