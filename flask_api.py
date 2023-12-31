from flask import Flask, request
import pandas as pd
import pickle

from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

with open('rfc.pkl', 'rb') as file:
    rfc = pickle.load(file)

@app.route('/')
def welcome():
    return 'Welcome'

@app.route('/predict')
def predict_note_authentication():
    
    """Bank Note Authentication
    This is using docstrings for specifications.
    ---
    parameters:
        - name: variance
          in: query
          type: number
          required: true
        - name: skewness
          in: query
          type: number
          required: true
        - name: curtosis
          in: query
          type: number
          required: true
        - name: entropy
          in: query
          type: number
          required: true
    responses:
        200:
            description: The Output values
    """
    variance=request.args.get("variance")
    skewness=request.args.get("skewness")
    curtosis=request.args.get("curtosis")
    entropy=request.args.get("entropy")
    prediction=rfc.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    
    return "The predicted value is "+ str(prediction)

@app.route('/predict_file', methods = ['POST'])
def predict_note_file():
    
    """Bank Note Authentication
    This is using docstrings for specifications.
    ---
    parameters:
        - name: file
          in: formData
          type: file
          required: truee
    responses:
        200:
            description: The Output values
    """
    df_test = pd.read_csv(request.files.get('file'))
    prediction = rfc.predict(df_test)
    return "The predicted value for the csv is "+str(list(prediction))

if __name__ == '__main__':
    app.run(debug=True)