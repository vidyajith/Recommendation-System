
import streamlit as st
import pickle
import pandas as pd
import requests   #for connecting with the API for getting film posters


st.title("MOVIE RECOMMENDER SYSTEM")

def fetch_poster(movie_id):
          response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=270184d5da16223dd148df6b7628d008&language=en-US'.format(movie_id))
          data =response.json()
          #print(data['poster_path'])
          return "https://image.tmdb.org/t/p/w500" + data["poster_path"]

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distance = similarity[index]
    movies_list =sorted(list(enumerate(distance)),reverse=True,key = lambda x: x[1])[1:6]
    recommended_movies =[]
    recommended_movie_posters = []
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id      #for fetching posters
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id)) # fetch poster from tmdb api
    return recommended_movies,recommended_movie_posters
movies_dict=pickle.load(open('movie_dict.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))
movies=pd.DataFrame(movies_dict)
selected_movie_name = st.selectbox(
    'Select a movie for recommendation',
     movies['title'].values)
if st.button('Recommend Movies'):
    name,poster=recommend(selected_movie_name)
    col1,col2,col3,col4,col5=st.beta_columns(5)
    with col1:
        st.header(name[0])
        st.image(poster[0])
    with col2:
        st.header(name[1])
        st.image(poster[1])
    with col3:
        st.header(name[2])
        st.image(poster[2])
    with col4:
        st.header(name[3])
        st.image(poster[3])
    with col5:
        st.header(name[4])
        st.image(poster[4])
st.text("BY VIDYA CHANDRAN.G")
st.text("INTERN,ORACUZ INFOTECH")

