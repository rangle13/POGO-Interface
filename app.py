from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Rod'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/changeTime')
def change_time():
    return "Returning a change in time."

@app.route('/tutorial')
def tutorial():
    return render_template('main.html')

if __name__ == '__main__':
    app.run()
