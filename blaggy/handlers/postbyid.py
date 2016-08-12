import webapp2
from models import BlogModel
import templater
from cookies import getUserFromRequest


class BlogHandler(webapp2.RequestHandler):
    # show the blog with the id
    def get(self, blog_id):
        post = BlogModel.get_by_id(int(blog_id))  # type:BlogModel
        if post:
            sign_activity = 'Signout' if getUserFromRequest(self.request) else 'Signin'
            sign_activity_link = 'signout' if sign_activity else 'signin'
            self.response.write(
                templater.render_a_post(post=post,
                                        sign_activity=sign_activity,
                                        sign_activity_link=sign_activity_link)
            )
        else:
            self.response.write("blog entry not found")
