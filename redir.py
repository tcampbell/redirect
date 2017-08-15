import flask
import yaml


app = flask.Flask(__name__)
url_map = yaml.load(open('urls.yml'))


# reserve admin actions first
@app.route('/reload')
def reload():
    # FIXME don't use a global
    global url_map
    url_map = yaml.load(open('urls.yml'))


@app.route('/<string:short_link>')
def index(short_link):
    if short_link not in url_map:
        return flask.abort(404)
    # TODO log and monitor the redirection
    return flask.redirect(url_map[short_link], code=302)
