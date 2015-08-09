import fresh_tomatoes
import media

#This file creates 6 instances of the movie class which hold informations about the favourite movies. 
despickable_me = media.Movie("Despicable Me", 
                        "When a criminal mastermind uses a trio of orphan girls as pawns for a grand scheme, he finds their love is profoundly changing him for the better",
                        "https://upload.wikimedia.org/wikipedia/en/d/db/Despicable_Me_Poster.jpg",
                        "https://www.youtube.com/watch?v=RXZY_XRjABs")

avatar = media.Movie("Avatar", 
                        "A Paraplegic Marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home...",
                        "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY")

iron_man = media.Movie("Iron Man", 
                        "After being held captive in an Afghan cave, an industrialist creates a unique weaponized suit of armor to fight evil.",
                        "https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG",
                        "https://www.youtube.com/watch?v=8hYlB38asDY")

transformers = media.Movie("Transformers", 
                        "An ancient struggle between two Cybertronian races, the heroic Autobots and the evil Decepticons, comes to Earth, with a clue to the ultimate power held by a teenager.",
                        "https://upload.wikimedia.org/wikipedia/en/9/94/Transformers_Age_of_Extinction_Poster.jpeg",
                        "https://www.youtube.com/watch?v=gAjgXlvVexI")

bourne_identity = media.Movie("Bourne Identity", 
                        "A man is picked up by a fishing boat, bullet-riddled and suffering from amnesia, before racing to elude assassins and regain his memory.",
                        "https://upload.wikimedia.org/wikipedia/en/a/ae/BourneIdentityfilm.jpg",
                        "https://www.youtube.com/watch?v=FpKaB5dvQ4g")


untouchables = media.Movie("Untouchables", 
                        "Federal Agent Eliot Ness sets out to stop Al Capone; because of rampant corruption, he assembles a small, hand-picked team.",
                        "https://upload.wikimedia.org/wikipedia/en/9/92/UntouchablesThe.jpg",
                        "https://www.youtube.com/watch?v=YbzkK06MJjE")

#the movies will be saved into a list of movies
movies = [despickable_me, avatar, iron_man, transformers, bourne_identity, untouchables]

#this command creates the movie page 
fresh_tomatoes.open_movies_page(movies)


