import flask
app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.redirect('https://github.com', code=302)
