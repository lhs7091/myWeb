from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content':'First post content',
        'date_posted': 'April 20 2018'
    },
    {
        'author': 'Lee Heesoo',
        'title': 'Flask Project',
        'content': 'First Flask',
        'date_posted': 'April 26 2020'
    }
]

@app.route("/")
@app.route("/home")
def hello():
    #return "<h1>Hello Flask</h1>"
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title="About")
    #return "<h1>About Flask</h1>"


if __name__ == '__main__':
    app.run(debug=True)


