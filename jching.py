import flask

app = flask.Flask(__name__)

from features import config, post

config = config.get_config('config.yaml')
post_list = post.get_post_list(config['post_dir'])

@app.route("/")
def index():
    return flask.render_template(
        'index.html',
        color_palette = config['color_palette'],
        tag_color = config['tag_color'],
        post_list = post_list
    )
