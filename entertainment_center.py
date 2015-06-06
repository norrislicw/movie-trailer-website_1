'''
This file entertainment_center.py provides codes for creating instances
with the class "Movie", and each instance is provided information
e.g. movie title, Youtube trailer URL, etc.
'''

import media
import fresh_tomatoes

# Provide information of each movie below, by using the class Movie
kingsman = media.Movie(
            "Kingsman",
            2014,
            "photos/kingsman.jpg",
            "https://www.youtube.com/watch?v=kl8F-8tR8to",
            "A spy organization recruits an unrefined but promising street \
            kid, and saves the world from a twisted tech genius.")
yes_man = media.Movie(
            "Yes Man",
            2008,
            "photos/yes_man.jpg",
            "https://www.youtube.com/watch?v=M3ar1tBj_Zk",
            "A guy challenges himself to say yes to everything for an entire \
            year, and his life starts to change.")
about_time = media.Movie(
            "About Time",
            2013,
            "photos/about_time.jpg",
            "https://www.youtube.com/watch?v=khB_wpn-bmc",
            "Tim discovers he can travel in time and change what has happened \
            in his own life, but not as easily as thought.")
unstoppable = media.Movie(
            "Unstoppable",
            2010,
            "photos/unstoppable.jpg",
            "https://www.youtube.com/watch?v=JM-0Ywc7wNY",
            "With an unmanned freight train rushing toward a city, a veteran \
            engineer and a young conductor race against the clock to prevent \
            a catastrophe.")
inception = media.Movie(
            "Inception",
            2010,
            "photos/inception.jpg",
            "https://www.youtube.com/watch?v=8hP9D6kZseM",
            "A thief who steals corporate secrets with the use of \
            dream-sharing  technology is given the inverse task of planting \
            an idea into the mind of a CEO.")
seven = media.Movie(
            "Se7en",
            1995,
            "photos/seven.jpg",
            "https://www.youtube.com/watch?v=J4YV2_TcCoE",
            "Two detectives, a rookie and a veteran, hunt a serial killer who \
            uses the seven deadly sins as his modus operandi.")

# Feel free to add Movie instances above this line

# Group the movies together in a list
movie_list = [kingsman, yes_man, about_time, unstoppable, inception, seven]

# Create or overwrite a webpage showing the movies' information
fresh_tomatoes.open_movies_page(movie_list)
