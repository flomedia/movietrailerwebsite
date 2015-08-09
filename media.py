import webbrowser

#this is the definition of the movie class
class Movie():
#this method initializes the movie with the relevant details
        def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
                self.title = movie_title
                self.storyline = movie_storyline
                self.poster_image_url = poster_image
                self.trailer_youtube_url = trailer_youtube
#this method starts the trailer from the link provided
        def show_trailer(self):
                webbrowser.open(self.trailer_youtube_url)
	    
	
