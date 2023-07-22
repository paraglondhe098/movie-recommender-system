import pandas as pd
import streamlit as st
import pickle
import requests



class MovieRecommender:
    def __init__(self,data,similarity):
        self.data=data
        self.similarity=similarity

    def get_cosine_similarities(self, index=0):
        return sorted(list(enumerate(self.similarity[index])), reverse=True, key=lambda x: x[1])

    def index_of(self, title):
        return self.data[self.data['title'] == title].index[0]

    @staticmethod
    def fetch_poster(movie_id):
        url = "https://api.themoviedb.org/3/movie/{}".format(movie_id)

        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwMTkwYmM5MTYyYmM2OWFmNGY1ZDVjMGE0Yzk5OTRlNiIsInN1YiI6IjY0YmE2NjA2MDZmOTg0MDBjNGYxZDk3NiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ezzVoyq7HDL2UnupEdYLbxrjrglnZgKSgJJV03_johc"
        }

        response = requests.get(url, headers=headers)
        poster_path=response.json()['poster_path']
        return "https://image.tmdb.org/t/p/original/"+poster_path
    def recommend(self, input_movie="Avatar", numbers=5):
        movie_index = self.index_of(input_movie)
        movies_list = self.get_cosine_similarities(movie_index)[1:numbers + 1]
        recommended = []
        recommended_posters=[]
        for i in movies_list:
            movie_id=self.data.iloc[i[0]].movie_id
            recommended.append(self.data.iloc[i[0]].title)
            recommended_posters.append(self.fetch_poster(movie_id))
        return recommended,recommended_posters


if __name__ == '__main__':
    movielist = pickle.load(open('Data/movies.pkl', 'rb'))
    similarity = pickle.load(open('Data/similarity.pkl', 'rb'))
    movies = pd.DataFrame(movielist)

    mr = MovieRecommender(movies,similarity)

    st.title("Movie Recommender System")
    selected_movie = st.selectbox(
        'Enter The Movie name',
        movies['title'])
    number = st.number_input('Number of recommendations',value=5)
    if st.button('Recommend',use_container_width=True):
        recommended_movies,recommended_movies_posters = mr.recommend(selected_movie, number)
        collist= st.columns(number)
        counter=0
        for i in collist:
            with i:
                st.image(recommended_movies_posters[counter])
                st.write(recommended_movies[counter])
                counter+=1