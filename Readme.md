
# movie-recommender-system

A content-based movie recommender system using bag of words vectorization and cosine similarities.

Requirements are listed in requirements.txt for the app file and requirements-jupyter.txt for the notebook (ipynb) file
## Data used

 - [TMDB movies credits](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_credits.csv)
 - [TMDB movies info](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv)

### How to generate data
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

![App Screenshot](https://github.com/paraglondhe098/movie-recommender-system/blob/master/Screenshot/AvatarExample.png)

