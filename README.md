# Spotify Song Recommender

## Overview
The Spotify Song Recommender is your musical companion, designed to elevate your listening experience. By harnessing the expansive Spotify music database and the art of data science, this application delivers personalised music suggestions tailored to your unique tastes.

## Motivation
I embarked on a mission to create a song recommender for Spotify with the aim of helping users discover new music that truly resonates with them. To accomplish this, I embraced the power of clustering algorithms to recommend music genres and styles based on the attributes of the input song.

## How It Works
Here's a breakdown of how our program functions:

1. **Input Song and Artist:** You provide the name of a song and its artist.
2. **Top 200 Check:** The program checks if the input song is among Spotify's top 200 songs. If it is, the recommender suggests another track from this exclusive list.
3. **Clustering Magic:** If your song isn't in the top 200, the program delves into a curated dataset containing songs with similar characteristics. These songs are grouped into clusters.
4. **Recommendation Time:** Based on the cluster analysis, the recommender suggests a song and artist that share attributes with your input.

## Code Style
My project makes use of several technologies and tools, including:

- **Python:** The primary programming language behind this project.
- **API Wrapper - Spotipy:** This library facilitates interactions with the Spotify API, granting us access to a rich source of music data.
- **KMeans Clustering:** I employed KMeans clustering to categorise songs with similar features, enabling personalised recommendations.
- **Beautiful Soup:** Beautiful Soup is instrumental in web scraping and data extraction of current music charts.

## Credits
I would like to credit the data sources that made this project possible:

- **Spotify Data:** The heart of my project, sourced through the Spotify API.
- **Billboard Top 100:** Valuable insights into popular music trends were derived from the Billboard charts. Explore them [here](https://www.billboard.com/charts/greatest-hot-100-singles/).
- **Pop Vortex:** Additional music charts and data were obtained from [Pop Vortex](https://www.popvortex.com/music/charts/top-100-songs.php).

Thank you for choosing my Spotify Song Recommender. I hope it brings a harmonious touch to your musical journey!
