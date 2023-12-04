from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/num_start', methods=['GET'])
def num_start():
    return render_template('chart.html')

if __name__ == '__main__':
    app.run(debug=True)
