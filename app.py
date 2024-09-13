import streamlit as st
import pandas as pd
import pickle
import requests



movie_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movie_dict)
st.title("Movie Recommendation System")
similarity=pickle.load(open('similarity.pkl','rb'))
def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distance=similarity[movie_index]
    movie_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    for i in movie_list:
        movie_id=movies.iloc[i[0]]['movie_id']
        recommended_movies.append(movies.iloc[i[0]]['title'])
    return recommended_movies

selected_movie_name=st.selectbox("Enter the name of the movie",movies['title'].values)


if st.button('Recommend'):
   names=recommend(selected_movie_name)
   col1,col2,col3,col4,col5=st.columns(5)

   with col1:
       st.text(names[0])
   with col2:
       st.text(names[1])
   with col3:
       st.text(names[2])
   with col4:
       st.text(names[3])
   with col5:
       st.text(names[4])