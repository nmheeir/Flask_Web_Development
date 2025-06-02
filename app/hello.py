from flask import Flask, request, make_response, redirect

app = Flask(__name__)

@app.route('/')
def index():
    response = make_response('This is a test')
    response.set_cookie('username', 'John Doe')
    return response

@app.route('/to_gg')
def to_gg():
    return redirect('https://www.google.com')

@app.route('/user/<username>')
def show_user(username):
    return f'User: {username}'

if __name__ == '__main__':
    app.run(debug=True)

