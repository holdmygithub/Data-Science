import findspark
findspark.init()
from pyspark.sql import SparkSession
from pyspark.ml.classification import LinearSVCModel
from pyspark.ml.pipeline import PipelineModel
from flasgger import Swagger
from flask import Flask,request,jsonify,redirect
#Load feature_pipe and model

feature_pipe = PipelineModel.load('feature_pipe')
model = LinearSVCModel.load('bank_note_model_svc')
spark = SparkSession.builder.master('local').appName('deployPyspark').getOrCreate()

app = Flask(__name__)
Swagger(app)

def predict(variance,skewness,curtosis,entropy,spark):
  print(type(variance))
  schema = "variance FLOAT, skewness FLOAT, curtosis FLOAT, entropy FLOAT"
  data = spark.createDataFrame([[variance,skewness,curtosis,entropy]],schema=schema)
  data = feature_pipe.transform(data)
  prediction = model.transform(data).select("prediction_svc").collect()[0][0]
  return "Fake Note" if(prediction) else "Authentic Note"

@app.route('/')
def noteAuth():
  return redirect("/apidocs/#/default/get_predict")

@app.route('/predict',methods = ["Get"])
def ask():

  """Authenticate bank notes
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
          description: The output values

  """
  variance = float(request.args.get("variance"))
  skewness = float(request.args.get("skewness"))
  curtosis = float(request.args.get("curtosis"))
  entropy =  float(request.args.get("entropy"))
  
  return predict(variance,skewness,curtosis,entropy,spark)


if __name__ == '__main__':
  app.run(host='0.0.0.0',port=8000)