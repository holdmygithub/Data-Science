from pyspark.sql import SparkSession
from pyspark.ml.classification import LinearSVCModel
from pyspark.ml.pipeline import PipelineModel
import streamlit as st
#Load feature_pipe and model

feature_pipe = PipelineModel.load('feature_pipe')
model = LinearSVCModel.load('bank_note_model_svc')
spark = SparkSession.builder.master('local').appName('deployPyspark').getOrCreate()

def predict(variance,skewness,curtosis,entropy,spark):
  schema = "variance FLOAT, skewness FLOAT, curtosis FLOAT, entropy FLOAT"
  data = spark.createDataFrame([[variance,skewness,curtosis,entropy]],schema=schema)
  data = feature_pipe.transform(data)
  prediction = model.transform(data).select("prediction_svc").collect()[0][0]
  return "Fake Note" if(prediction) else "Authentic Note"
    
def noteAuth():
    st.title("Bank Note Authentication")
    st.markdown("Application for predicting the authenticity of Bank Notes")

    variance = float(st.text_input("Variance", 3.6216))
    skewness = float(st.text_input("Skewness",8.6661))
    curtosis = float(st.text_input("Curtosis",-2.8073))
    entropy = float(st.text_input("Entropy",-0.44699))

    if(st.button("Predict")):
      result = predict(variance,skewness,curtosis,entropy,spark)
      st.success(f"Prediction: {result}")

if __name__ == '__main__':
  noteAuth()
