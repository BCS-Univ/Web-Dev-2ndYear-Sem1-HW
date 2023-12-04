from flask import Flask, render_template
from datetime import datetime

import os

app = Flask(__name__)

@app.route('/')
def pageAppInfo():
    with open('b06/data.txt', 'a+') as f:
        f.write(str(datetime.now()) + '\n')
        f.seek(0)  # reset file read/write pointer to the beginning
        connection_times = f.read()

    return render_template('index.html', connection_times=connection_times, title="Python Flask !")

if __name__ == '__main__':
    app.run(debug=True, port=5500)