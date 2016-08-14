# Appstory
A multi-user blog using webapp2-python and Bootstrap that can be readily deployed to Google App Engine.

Built with
==========
- Python
- Google App Engine
- webapp2
- Bootstrap3
- Jinja2
- Iconmoon fonts

How to use
==========
This app can be deployed to GAE or run locally by Launcher Application.

Functionality
============
1. User Accounts:
  Users account activity is implemented using secured cookies. Usernames are maintained to be unique. The password is stored as Hash values with salted compound.
  User activities
  - Sign-up
  - Sign-in 
  - Sign-out 
2. Blog Posts:
  Registered users can post to the blog. That post can later be edited or deleted by the author.
3.  Commenting:
  Posts can be commented by any of registered user. Unregistered users can view the comments. Registered users can edit or delete their own comments.
4.  Like/Dislike:
  Each of the post can be like/disliked by other registered users (Not the Author). User can't dislike a post if they haven't already liked it.

The app is available on GAE at 
https://appstory-140311.appspot.com/blog/all
