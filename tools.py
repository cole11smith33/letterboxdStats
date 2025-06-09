from letterboxdpy import user

def setUser():
    username = input(str("Please enter the username of the letterboxd account you wish to see the statistics for: "))
    username = user.User(username)
    print(username)