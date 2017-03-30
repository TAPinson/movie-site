#import fresh_tomatoes.py which will generate our website
import fresh_tomatoes
#import media.py for class Movie
import media

#object template:
#movie_name = media.Movie("title",
#                         "movie_storyline",
#                         "poster_image",
#                         "trailer_youtube")

toy_story = media.Movie("Toy Story",
                        "Are we playing with the toys? Or are they playing with us?",
                        "http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg",
                        "https://youtu.be/BuNF7Z7sAt8")

the_princess_bride = media.Movie("The Princess Bride",
                                 "The Dread Pirate Roberts stalks the fiancee of the noble Prince Humperdink after hearing of their engagement. ",
                                 "http://shelbyparkpictureshow.com/wp-content/uploads/2016/07/the-princess-bride-poster.jpg",
                                 "https://youtu.be/wURAWg_uW_c")

the_shawshank_redemption = media.Movie("The Shawshank Redemption",
                                       "The heart-warming story of bromance and preserverance.",
                                       "https://images-na.ssl-images-amazon.com/images/M/MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._V1_UY1200_CR88,0,630,1200_AL_.jpg",
                                       "https://youtu.be/qmWUIndki10")

the_lion_king = media.Movie("The Lion King",
                            "It's the circle of life... with lions!",
                            "https://s-media-cache-ak0.pinimg.com/originals/bf/94/d6/bf94d68ae27c2320801ff34d84ae962e.jpg",
                            "https://youtu.be/4sj1MT05lAA")

back_to_the_future = media.Movie("Back to the Future",
                                     "Marty travels in time to 1955",
                                     "http://cineplexfiles.s3.amazonaws.com/Promos/BacktotheFuture/BTTF_header2.jpg",
                                     "https://youtu.be/qvsgGtivCgs")
                                     

back_to_the_future_two = media.Movie("Back to the Future II",
                                     "Marty travels in time to 2015",
                                     "https://upload.wikimedia.org/wikipedia/en/c/c2/Back_to_the_Future_Part_II.jpg",
                                     "https://youtu.be/VLBvaL0-AsI")

back_to_the_future_three = media.Movie("Back to the Future III",
                                       "Marty travels in time to 1885",
                                       "http://www.seeing-stars.com/Locations/BTTF-3/BTTF3-Poster.jpg",
                                       "https://youtu.be/EYkguxpqsrg")


willy_wonka = media.Movie("Willy Wonka & the Chocolate Factory",
                          "A golden ticket, and a world of pure imagination!",
                          "http://resizing.flixster.com/O8fmNIoHSFQS4J4sGqZEa8HOiyE=/800x1200/v1.bTsxMTE2ODA4NTtqOzE3MzQ5OzIwNDg7ODAwOzEyMDA",
                          "https://youtu.be/2cBja3AbahY")

#lists movies to show Movie instances on fresh_tomatoes.py
movies = [toy_story, the_princess_bride, the_shawshank_redemption, the_lion_king, back_to_the_future, back_to_the_future_two, back_to_the_future_three, willy_wonka]
fresh_tomatoes.open_movies_page(movies)


