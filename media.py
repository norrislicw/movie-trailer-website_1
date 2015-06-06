'''
This file media.py provides codes for defining a class "Movie"
'''


class Movie():
    def __init__(self, title, release_year, poster_image_url,
                 trailer_youtube_url, description=""):
        # Initialize an instance
        self.title = title
        self.release_year = release_year
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.description = description

    def get_title(self):
        # Return the title of the movie
        return self.title
