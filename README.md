# 🎬 Movie Recommender System

A machine learning–powered movie recommendation system developed with Streamlit that delivers personalized movie suggestions using content-based filtering and integrates with the TMDB API for rich metadata.

## Overview

This project implements a content-based movie recommendation system that analyzes movie attributes such as genres, cast, crew, and keywords to identify similar movies based on user input. The application enhances user experience by dynamically fetching movie posters and metadata from The Movie Database (TMDB) API.


## Features

- **Interactive Web Interface**: Built with Streamlit for easy accessibility
- **Content-Based Recommendations**: Uses similarity metrics to find movies with comparable characteristics
- **Dynamic Poster Display**: Fetches movie posters from TMDB API
- **Movie Selection**: Browse through 5000+ movies from the TMDB dataset
- **Real-time Processing**: Generates recommendations instantly upon user request

## Project Structure

```
Movie-recommended-system/
├── app.py                          # Main Streamlit application
├── config.py                       # Configuration file (API keys)
├── requirements.txt                # Python dependencies
├── Movie-recommended-system.ipynb   # Jupyter notebook with data processing
├── Dataset/
│   ├── tmdb_5000_credits.csv      # Movie credits data
│   └── tmdb_5000_movies.csv       # Movie metadata
├── movies_dict.pkl                 # Processed movies dictionary (pickle)
├── similarity.pkl                  # Similarity matrix (pickle)
└── README.md                       # Project documentation
```

## Prerequisites

- Python 3.7+
- pip (Python package manager)
- TMDB API key (free at [themoviedb.org](https://www.themoviedb.org/settings/api))

## Installation

1. **Clone or download the project**:
   ```bash
   cd Movie-recommended-system
   ```

2. **Create a virtual environment (optional but recommended)**:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Linux/Mac:
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your TMDB API key** (if not already configured):
   - Sign up at [TMDB API](https://www.themoviedb.org/settings/api)
   - Update the `API_KEY` in [config.py](config.py)

## Usage

Run the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your default browser (usually at `http://localhost:8501`).

### How to Use:

1. **Select a Movie**: Choose a movie from the dropdown menu
2. **Get Recommendations**: Click the "Recommend" button
3. **View Results**: Browse the 5 recommended movies with their posters
4. **Repeat**: Select another movie to get new recommendations

## Data Processing

The project uses data from the TMDB 5000 Movies and Credits datasets:

- **Movies Data**: Contains metadata like genre, overview, budget, revenue, etc.
- **Credits Data**: Contains cast and crew information

The Jupyter notebook ([Movie-recommended-system.ipynb](Movie-recommended-system.ipynb)) handles:
- Data loading and cleaning
- Feature extraction and engineering
- Similarity matrix computation
- Pickling models for production use

## Technical Stack

- **Framework**: Streamlit (web UI)
- **Data Processing**: Pandas, NumPy
- **Machine Learning**: Scikit-learn (similarity metrics)
- **API Integration**: TMDB API via requests
- **Data Serialization**: Pickle

## Key Dependencies

- `streamlit` - Web application framework
- `pandas` - Data manipulation
- `numpy` - Numerical computing
- `scikit-learn` - Machine learning utilities
- `requests` - HTTP library for API calls
- `pickle` - Model serialization

## How It Works

1. **Content-Based Filtering**: The system computes a similarity matrix between movies based on:
   - Genres
   - Cast and crew
   - Keywords and overview
   - Other metadata

2. **Recommendation Logic**:
   - User selects a movie
   - System finds the movie's index
   - Retrieves top 5 movies with highest similarity scores (excluding the selected movie)
   - Fetches posters from TMDB API

3. **Poster Fetching**: Uses TMDB API to dynamically retrieve movie posters with error handling and fallback placeholders


## Dataset Source

- [TMDB 5000 Movies & Credits](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- Movie posters: [TMDB API](https://www.themoviedb.org/settings/api)


## 🌐 Connect here <p align="left">

<a href="https://linkedin.com/in/anushka-gupta18" target="blank"> <img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="anushka-gupta18" height="30" width="40" /> </a> </p>