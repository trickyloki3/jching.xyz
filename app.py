import flask

from features import config, post, form

config = config.get_config('config.yaml')
post_dict = post.get_post_dict(config['post_folder'])

app = flask.Flask(
    config['app_name'],
    static_folder = config['file_folder'],
    template_folder = config['temp_folder']
)

@app.route("/")
def index(group = 'index'):
    return flask.render_template(
        'index.html',
        **config,
        group = group,
        column_list = post.get_column_list(post_dict[group], flask.request.args.get('tag'))
    )

@app.route("/<group>", methods = ['GET', 'POST'])
def group(group):
    if group not in post_dict:
        return flask.redirect(flask.url_for('index'))

    if flask.request.method == 'POST' and group in post_dict:
        form.put_form(config['form_folder'], group, flask.request.form)

    return flask.render_template(
        'index.html',
        **config,
        group = group,
        column_list = post.get_column_list(post_dict[group], flask.request.args.get('tag'))
    )
