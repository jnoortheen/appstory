from google.appengine.ext import db
import templater
from datetime import datetime
import hmac

class UserModel(db.Model):
    name = db.StringProperty(required=True)
    pwd = db.StringProperty(required=True)
    salt = db.StringProperty()
    email = db.EmailProperty()
    created_time = db.DateTimeProperty(auto_now_add=True)

    def __init__(self, *args, **kwargs):
        kwargs['salt'] = datetime.now().strftime("%d%m%y%H%M%S")
        kwargs['pwd'] = hmac.new(kwargs['salt'], kwargs['pwd']).hexdigest()
        super(UserModel, self).__init__(*args, **kwargs)

    def render(self):
        return templater.render_welcome_page(user=self)
