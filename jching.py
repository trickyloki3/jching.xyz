import flask

app = flask.Flask(
    __name__,
    static_folder='files',
    template_folder='templates'
)

from features import config, post

config = config.get_config('config.yaml')
post_list = post.get_post_list(config['post_folder'])

@app.route("/")
def index():
    return flask.render_template(
        'index.html',
        **config,
        post_list = post.filter_post_list(post_list, tag = flask.request.args.get('tag'))
    )

@app.route("/<meta>")
def filter_by_meta(meta):
    return flask.render_template(
        'index.html',
        **config,
        post_list = post.filter_post_list(post_list, meta = meta)
    )
