# ------------- WAVE 1 --------------------
# Create create_movie function that adds movies (title, genre, rating) to a dictionary
def create_movie(title, genre, rating):
    movie_dict = {}
    movie_dict["title"] = title
    movie_dict["genre"] = genre
    movie_dict["rating"] = rating
    
    for category in movie_dict:
        if movie_dict[category] == None:
            return None
    
    print(movie_dict)
    return movie_dict

# Create add_to_watched function that adds movies that a user has watched to a dict
def add_to_watched(user_data, movie):
    watched_list = []
    watched_list.append(movie)
    user_data["watched"] = watched_list

    print(user_data)
    return user_data

# Create add_to_watchlist function that adds movies to a user's watchlist in a dict
def add_to_watchlist(user_data, movie):
    watchlist = []
    watchlist.append(movie)
    user_data["watchlist"] = watchlist

    print(user_data)
    return user_data

# Create watch_movie function that moves movies from watchlist to watched list
def watch_movie(user_data, movie_to_watch):
    for i in range(len(user_data["watchlist"])):
        if user_data["watchlist"][i]["title"] == movie_to_watch:
            movie_watched = user_data["watchlist"][i]
            user_data["watched"].append(movie_watched)
            user_data["watchlist"].remove(movie_watched)
    
    print(user_data)
    return user_data
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

# Creat get_watched_avg_rating function
def get_watched_avg_rating(user_data):
    total_watched_rating = 0
    for i in range(len(user_data["watched"])):
        total_watched_rating += user_data["watched"][i]["rating"]

    if user_data["watched"] == []:
        return 0.0
    else:
        avg_rating = total_watched_rating / len(user_data["watched"])
        return avg_rating

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------