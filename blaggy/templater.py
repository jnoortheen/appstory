import os
import jinja2

JINJA_ENV = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates")),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
)


def render_signup_page(**kwargs):
    template = JINJA_ENV.get_template('sign-up.html')
    return template.render(**kwargs)

def render_signin_page(**kwargs):
    template = JINJA_ENV.get_template('sign-in.html')
    return template.render(**kwargs)


def render_welcome_page(**kwargs):
    template = JINJA_ENV.get_template('welcome.html')
    return template.render(**kwargs)


def render_a_post(**kwargs):
    template = JINJA_ENV.get_template('a-post.html')
    return template.render(**kwargs)


def render_all_post(**kwargs):
    template = JINJA_ENV.get_template('all-posts.html')
    return template.render(**kwargs)


def render_new_post(**kwargs):
    template = JINJA_ENV.get_template('new-post.html')
    return template.render(**kwargs)
