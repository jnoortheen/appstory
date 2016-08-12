from google.appengine.ext import db
from datetime import datetime
from .UserModel import UserModel


class BlogModel(db.Model):
    title = db.StringProperty(required=True)  # type: str
    content = db.TextProperty(required=True)  # type: str
    # username of writer
    author = db.ReferenceProperty(UserModel, collection_name='posts')  # type:UserModel
    created_time = db.DateTimeProperty(auto_now_add=True)  # type:datetime
    modified_time = db.DateTimeProperty(auto_now=True)

    def get_content(self, truncate=False):
        if truncate:
            return ("\n".join(self.content.split('\n')[:10])).replace('\n', "<br/>")
        return self.content.replace("\n", "<br/>")

    def get_created_time(self):
        return self.created_time.strftime("%d-%m-%y %I:%M:%S%p")

    def get_perma_link(self):
        return "/blog/%s" % (self.key().id())

    def get_author_name(self):
        return "Anonymous" if not self.author else self.author.name
