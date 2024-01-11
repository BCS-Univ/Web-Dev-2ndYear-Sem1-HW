from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')  # The navigation bar should be part of this template.

@app.route('/page1')
def page1():
    return 'Page 1'

@app.route('/page2')
def page2():
    return 'Page 2'

@app.route('/page3')
def page3():
    return 'Page 3'

@app.route('/list/page1')
def list_page1():
    return 'Subpage 1'

@app.route('/list/page2')
def list_page2():
    return 'Subpage 2'

@app.route('/list/page3')
def list_page3():
    return 'Subpage 3'

if __name__ == '__main__':
    app.run(debug=True)
