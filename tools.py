from letterboxdpy import user

def setUser():
    name = input(str("Please enter the username of the letterboxd account you wish to see the statistics for: "))
    username = user.User(name) # stored as type letterboxdpy.user.User
    #print(type(username))
    #print(username.stats)
    #print(username.watchlist_length)

def getUserGenreInfo(username):
    try:
        print(user.user_genre_info(username))
    except:
        print("Not enough user information to view genre distribution")