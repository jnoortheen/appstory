import webapp2
import templater
from cookies import getUserFromRequest
import logging


class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("checking cookie %s" % self.request.cookies)
        user = getUserFromRequest(self.request)
        if user:
            self.response.write(
                templater.render_welcome_page(user=user,
                                              sign_activity='Signout',
                                              sign_activity_link='signout')
            )
        else:
            # redirect to sign up page in case user is not found in the db
            self.redirect("/signup")
