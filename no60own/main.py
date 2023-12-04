from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/num_start', methods=['GET', 'POST'])
def num_start():
    return 'empty'
    if request.method == 'POST':
        numbers = request.json.get('numbers')
        numbers = process_numbers(numbers)
        chart_data = numbers
        return json.dumps({'chartData': chart_data})
    return render_template('chart.html')

def process_numbers(numbers):
    numbers = numbers.split(',')
    numbers = [int(number) for number in numbers]
    print(numbers)
    return numbers


if __name__ == '__main__':
    app.run(debug=True)
