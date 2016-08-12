import webapp2
import templater
from models import UserModel
from cookies import getCookieHashForUserid
import logging


class SignoutHandler(webapp2.RequestHandler):
    def get(self):
        self.response.delete_cookie('user_id')
        self.redirect('/signin')


class SigninHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(templater.render_signin_page(
            errormsg=self.request.get('errmsg')))

    def post(self):
        username = self.request.get("userName")
        pwd = self.request.get("pwd")
        if username and pwd and getUserByName(username):
            user = getUserByName(username)
            self.response.set_cookie('user_id', str(getCookieHashForUserid(user.key().id())))
            self.redirect("/welcome")
        else:
            self.redirect('/signin?errormsg=invalid login')


class SignupHandler(webapp2.RequestHandler):
    def get(self):
        errormsg = self.request.get("errormsg")
        self.response.write(templater.render_signup_page(errormsg=errormsg))

    def post(self):
        username = self.request.get("userName")
        pwd = self.request.get("pwd")
        email = self.request.get("email")
        if username and pwd:
            if getUserByName(username):
                # username already exists
                self.redirect('/signup?errormsg=username_exists')
                return
            # add user to db
            user = UserModel(name=username, pwd=pwd, email=email)
            user.put()
            self.response.set_cookie('user_id', str(getCookieHashForUserid(user.key().id())))
            self.redirect("/welcome")
        else:
            self.redirect("/signup?errormsg=invalid_data")


def getUserByName(username):
    # check and return user db object
    return UserModel.all().filter("name = ", username).get()
