from flask import Flask, request, render_template
import os
import sys
from src.pipelines.prediction_pipeline import CustomData, PredictionPipeline
from src.exception import CustomException
from src.logger import logging

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('form.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        try:
            data = CustomData(
                carat=float(request.form.get('carat')),
                depth=float(request.form.get('depth')),
                table=float(request.form.get('table')),
                x=float(request.form.get('x')),
                y=float(request.form.get('y')),
                z=float(request.form.get('z')),
                cut=request.form.get('cut'),
                color=request.form.get('color'),
                clarity=request.form.get('clarity')
            )
            final_new_data = data.get_data_as_dataframe()
            predict_pipeline = PredictionPipeline()
            pred = predict_pipeline.predict(final_new_data)
            results = round(pred[0], 2)
            
            return render_template('result.html', 
                                 final_result=results,
                                 input_data=request.form)
            
        except Exception as e:
            logging.error(f"Error during prediction: {str(e)}")
            return render_template('error.html', error_message=str(e))
        
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)