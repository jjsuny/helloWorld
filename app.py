from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Jeff Jiang! Coding changes '

@app.route('/hello')
def hello():
    return render_template('hello.html')

#new changes for commit
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/about-css')
def about_css()
    return render_template('about-css.html')

if __name__ == '__main__':
    app.run()

