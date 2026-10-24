import streamlit as st 
import pickle
import requests #To import the website.. http://abc.com and to fetch the page details

movies = pickle.load(open('movie.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')
st.caption('This app follows content based recommendation syste,')
st.caption('Recommendation is based on movie generes, kewords, overview, top 4 cast members and directors')
st.text("Databse for this movie recommender is sourced from TMDB website")

movie_list = movies['title'].values
selected_movie = st.selectbox("Type or select a movie from dropdown",movie_list,index=None)

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=0f1fc318bfc3c532b6cb1ee6a83c69b6"
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/original/" + poster_path
    return full_path


def recommend(movie):
    index = movies[movies['title']==movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),key=lambda x:x[1],reverse=True)[1:6]
    recommended_movie_names = []
    recommended_poster_path = []
    for i in distances:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_poster_path.append(fetch_poster(movie_id))
    return recommended_movie_names, recommended_poster_path

if st.button("Show Recommendations"):
    st.write("Here are the similar movies to watch")
    recommended_movie_names, recommended_poster_path = recommend(selected_movie)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_poster_path[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_poster_path[1])
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_poster_path[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_poster_path[3])
    with col5:
        st.text(recommended_movie_names[4])  
        st.image(recommended_poster_path[4])  

