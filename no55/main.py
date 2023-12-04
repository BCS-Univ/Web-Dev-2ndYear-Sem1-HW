from flask import Flask, render_template
from dataExtractor import dataExtractor

app = Flask(__name__)

@app.route('/page/app')
def pageAppInfo():
    return render_template('page.html', data=dataExtractor(), title="Python Flask!")

if __name__ == '__main__':
    app.run(debug=True, port=5500)