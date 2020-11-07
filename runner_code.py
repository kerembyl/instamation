import functions_myinsta
from user_credentials import my_username, my_password

# Login
# Go to https://www.instagram.com and enter the login info provided in (user_credentials.py)
# You can comment out below this line if you are already logged in.
functions_myinsta.login_action(my_username, my_password)

# Like by tags
# Go to https://www.instagram.com/tags/ and loop through tags and like posts
tagList = ["coffeeaddict", "morningcoffee", "espresso"]
commentList = ["Great!", "Can't start my day without coffee, really.", "Nice post :)", "Great post!", "good work!", "we need sustainable coffee production, otherwise what we'd do?"]
functions_myinsta.like_by_tags(tagList, commentList, likePercent=35, commentAdd=True, followUser=True)   