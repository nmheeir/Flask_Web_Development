from flask import Flask, request, make_response, redirect, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)

bootstrap = Bootstrap()
moment = Moment()

bootstrap.init_app(app)
moment.init_app(app)

@app.route('/')
def index():
    return render_template('index.html', name = 'John', current_time = datetime.utcnow()), 404


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)

