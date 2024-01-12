from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', title='Home', heading='Home')

@app.route('/page1')
def page1():
    return render_template('home.html', title='Page 1', heading='Page 1')

@app.route('/page2')
def page2():
    return render_template('home.html', title='Page 2', heading='Page 2')

@app.route('/page3')
def page3():
    return render_template('home.html', title='Page 3', heading='Page 3')

@app.route('/list/page1')
def list_page1():
    return render_template('home.html', title='Subpage 1', heading='Subpage 1')

@app.route('/list/page2')
def list_page2():
    return render_template('home.html', title='Subpage 2', heading='Subpage 2')

@app.route('/list/page3')
def list_page3():
    return render_template('home.html', title='Subpage 3', heading='Subpage 3')

if __name__ == '__main__':
    app.run(debug=True)
