from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def chart():
    if request.method == 'POST':
        # Parse form data
        sales_data = {
            'ToothPaste': request.form.get('ToothPaste', type=int),
            'FaceCream': request.form.get('FaceCream', type=int),
            'FaceWash': request.form.get('FaceWash', type=int),
            'BathingSoap': request.form.get('BathingSoap', type=int),
            'Shampoo': request.form.get('Shampoo', type=int),
            'Moisturizer': request.form.get('Moisturizer', type=int)
        }
    else:
        # Default data
        sales_data = {
            'ToothPaste': 32,
            'FaceCream': 46,
            'FaceWash': 99,
            'BathingSoap': 34,
            'Shampoo': 77,
            'Moisturizer': 91
        }
    
    # Render the HTML template with the sales data
    return render_template('chart.html', sales_data=sales_data)

if __name__ == '__main__':
    app.run(debug=True)
