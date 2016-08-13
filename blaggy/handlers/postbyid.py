import webapp2
from models import BlogModel, UserModel
import templater
from cookies import getUserFromRequest


class BlogHandler(webapp2.RequestHandler):
    # show the blog with the id
    def get(self, blog_id):
        post = BlogModel.get_by_id(int(blog_id))  # type: BlogModel
        if post:
            user = getUserFromRequest(self.request)  # type: UserModel
            sign_activity = 'Signout' if user else 'Signin'
            sign_activity_link = 'signout' if sign_activity else 'signin'
            kwargs = {'post': post,
                      'sign_activity': sign_activity,
                      'sign_activity_link': sign_activity_link}
            if user and post.author.key().id() == user.key().id():
                kwargs['showEdit'] = True
            if self.request.get('like'):
                if user and user.key().id() != post.author.key().id():
                    # author of the post can't like his own
                    if self.request.get('like') == 'yes':
                        # add the like count if the user already didn't liked
                        if user.key().id() not in post.likes:
                            post.likes.append(user.key().id())
                    elif self.request.get('like') == 'no':
                        # reduce the like count and pop user id from list
                        if user.key().id() in post.likes:
                            post.likes.pop(user.key().id())
                elif not user:
                    # forward user to signin as they haven't logged in
                    self.redirect('/signin')
                    return

            self.response.write(
                templater.render_a_post(**kwargs)
            )
        else:
            self.response.write("blog entry not found")
