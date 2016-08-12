import webapp2
from models import BlogModel
import templater
from cookies import getUserFromRequest


class BlogsHandler(webapp2.RequestHandler):
    # list all the blog posts - default landing page
    def get(self):
        posts = BlogModel.all()
        posts.order('created_time')
        sign_activity = 'Signout' if getUserFromRequest(self.request) else 'Signin'
        sign_activity_link = 'signout' if sign_activity else 'signin'
        self.response.write(
            templater.render_all_post(posts=posts, sign_activity=sign_activity, sign_activity_link=sign_activity_link)
        )
