from flask import render_template, request
from app import app
from app.ml_model import predict_environmental_impact

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        product_name = request.form.get('product_name')
        result = predict_environmental_impact(product_name)  # Call to the ML function
    return render_template('index.html', result=result)

