
# movie-recommender-system

# Summary
 
**Movie Recommender System using Bag of Word Vectorization**

The Movie Recommender System using Bag of Word Vectorization is a data science project that incorporates a user-friendly Graphical User Interface (GUI) built using Streamlit. The GUI provides an intuitive platform for users to interact with the system, input their preferences, and receive personalized movie recommendations.

**Overview:**
The primary objective of this project is to offer movie enthusiasts an easy-to-use tool to discover new movies tailored to their interests. Leveraging the Bag of Word (BoW) vectorization method and content-based filtering, the system efficiently processes various movie attributes, including movie plot summaries, cast, directors, and genres, to suggest relevant movies based on user input.

**Bag of Word Vectorization:**
The Bag of Word (BoW) vectorization technique is employed to represent movie plot summaries as numerical feature vectors. By transforming the textual content into a numerical representation, BoW facilitates efficient comparison and similarity calculation between movies.

**Data Preprocessing:**
Before applying the BoW vectorization, the dataset undergoes thorough preprocessing, including text cleaning, tokenization, stopword removal, and stemming/lemmatization. These steps help eliminate noise and enhance the quality of the processed text data.

**Building the Recommender System:**
The project adopts a content-based filtering approach to generate movie recommendations. When a user provides their preferred movie or selects genres they enjoy, the system processes the input using BoW vectorization. It then computes similarity scores between the input movie and all other movies in the dataset using Cosine Similarity.

**Cosine Similarity:**
Cosine Similarity is a widely used metric for measuring the similarity between two non-zero vectors. In this context, it quantifies the similarity between the BoW vector representations of movies' plot summaries. The cosine similarity score ranges from -1 to 1, where 1 indicates perfect similarity, 0 indicates no similarity, and -1 indicates complete dissimilarity.

**Streamlit GUI:**
The GUI is developed using Streamlit, a popular Python library for creating web applications effortlessly. The interface allows users to access the movie recommender system without the need for coding knowledge or complex interactions. It presents a user-friendly input form where users can:

1. Enter the title of their favorite movie.
2. Select genres they enjoy from a predefined list of genres.
3. Set the number of movie recommendations they want to receive.

**Recommendation Generation:**
Once the user provides their input, the system processes the data, calculates similarity scores using Cosine Similarity, and generates personalized movie recommendations. The top N movies with the highest similarity scores are displayed as the final recommendations to the user on the Streamlit interface.

**Evaluation Metrics:**
To assess the effectiveness of the recommender system, evaluation metrics such as precision, recall, and F1-score are employed. These metrics measure the accuracy and relevancy of the system's recommendations.

**Conclusion:**
The Movie Recommender System using Bag of Word Vectorization with Streamlit GUI is a user-friendly and effective data science project that provides personalized movie recommendations. By leveraging the power of BoW vectorization, employing Cosine Similarity, and incorporating a user-friendly interface with Streamlit, the system enhances the movie-watching experience for users. It encourages them to explore and enjoy a wide range of films that align with their preferences and interests.


**--Requirements are listed in requirements.txt for the app file and requirements-jupyter.txt for the notebook (ipynb) file--**
## Data used

 - [TMDB movies credits](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_credits.csv)
 - [TMDB movies info](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv)

### To generate similarity data
* Download data from Kaggle (links are in Data Used section)
* Open notebook file
* Run every cell
* It will generate movies.pkl and similarity.pkl files
* These files can be used in an app file ( Because of their size, I was not able to include them here)
* Run app.py using streamlit
 ```bash
  streamlit run app.py
```
## Screenshots

![App Screenshot](https://upload.wikimedia.org/wikipedia/commons/3/38/ScreenshotMRS.png)




