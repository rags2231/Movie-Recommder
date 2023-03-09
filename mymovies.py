import streamlit as st
import pickle
import numpy as np
import pandas as pd


def recommend(movie):
    index=movies_list[movies_list.title==movie].index[0]
    distances=sorted(list(enumerate(similarity[index])),reverse=True,key=lambda x:x[1])
    recommended_movies=[]
    for i in distances[1:6]:
        movie_id=i[0]
        recommended_movies.append(movies_list.iloc[i[0]].title)
    return recommended_movies

similarity=pickle.load(open('similarity.pkl','rb'))
movies_dicto=pickle.load(open('movies_dict.pkl','rb'))
movies_list=pd.DataFrame(movies_dicto)

st.title('Movie Recommendation System')
st.caption('Where search ends !')
selected_movie = st.selectbox(
    'Type your movie',
    movies_list['title'].values
    )
if st.button('Recommend'):
    recommendations_list=recommend(selected_movie)
    for i in recommendations_list:
     st.write(i)