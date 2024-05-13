import flask

app = flask.Flask(
    __name__,
    static_folder='files',
    template_folder='templates'
)

from features import config, post, form

config = config.get_config('config.yaml')
post_list = post.get_post_list(config['post_folder'])
post_pinned_list = post.get_post_list(config['post_pinned_folder'])

@app.route("/")
def index():
    return flask.render_template(
        'index.html',
        **config,
        post_list = post.filter_post_list(post_list, tag = flask.request.args.get('tag')),
        post_pinned_list = post.filter_post_list(post_pinned_list, tag = flask.request.args.get('tag'))
    )

@app.route("/<meta>", methods = ['GET', 'POST'])
def meta(meta):
    if flask.request.method == 'POST':
        form.put_form(config['form_folder'], flask.request.form)

    return flask.render_template(
        'index.html',
        **config,
        post_list = post.filter_post_list(post_list, meta = meta, tag = flask.request.args.get('tag')),
        post_pinned_list = post.filter_post_list(post_pinned_list, meta = meta, tag = flask.request.args.get('tag'))
    )
