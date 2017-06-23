# importing the webbrowser module
import webbrowser


# Defining a movie class
class Movie():

    # A constant list of Valid Ratings
        VALID_RATINGS = ["G", "PG", "PG-13", "R"]

        def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
                """ The constructor is being defined which initialises various details of the movies to its instances.

                        Args:
                                1) Self: The first argument. This refers to the instance that uses it.
                                    For eg: self.story_line = story_line means that the story_line variable
                                                will have a seperate copy for each instance that calls it.

                                2) movie_title: Contains a string of Movie Title.

                                3) movie_storyline: Contains a string of the Movie Storyline which is
                                a short summary of the movie that succintly describes it.

                                4) poster_image: Contains a string of the link to the URL containing the image of the poster.

                                5) trailer_youtube: Contains a string of the link to the Youtube URL of the trailer.

    """
                self.title = movie_title
                self.storyline = movie_storyline
                self.poster_image_url = poster_image
                self.trailer_youtube_url = trailer_youtube

        def show_trailer(self):
            """ This function opens a web browser with the given youtube URL. """
            webbrowser.open(self.trailer_youtube_url)
