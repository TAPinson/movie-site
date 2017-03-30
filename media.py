#import webbrowser to launch fresh_tomatoes.py which is imported by entertainment_center.py
import webbrowser

#defining the class Movie constructor
#inputs: class template filled with instances from entertainment_center.py
#outputs: sends instances to fresh_tomatoes.py
class Movie():
    """This class provides a way to store movie related information"""
    def __init__(self,movie_title, movie_storyline, poster_image,trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    #launches webbrowser to specified trailer URL from trailer_youtube
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


