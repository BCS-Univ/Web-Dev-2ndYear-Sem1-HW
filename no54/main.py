from flask import Flask, render_template

app = Flask(__name__)

@app.route('/apple')
def apple():
    return render_template('apple.html')

@app.route('/text')
def text():
    return render_template('text.html')

if __name__ == '__main__':
    app.run(debug=True, port=5500)  