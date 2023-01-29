from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
  {
    'author': 'Miras Adilov',
    'title': 'Blog Post 1',
    'content': 'First post content',
    'date posted': 'Jan 28, 2023'
  },
    {
    'author': 'First Last',
    'title': 'Blog Post 2',
    'content': 'Second post content',
    'date posted': 'Jan 29, 2023'
  }
]

@app.route("/")
@app.route("/home")
def home_page():
  return render_template('home.html', posts=posts)


@app.route("/about")
def about():
  return render_template('about.html', title='About')




if __name__== '__main__':
  app.run(debug=True)