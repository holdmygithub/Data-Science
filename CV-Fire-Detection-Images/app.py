import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.image import resize
from tensorflow import expand_dims,round

model = load_model('modelsCNN/model_fire_detection.h5')
class_indices = {0:'fire',1:'no fire'}

def predict():
    img = Image.open(file)
    st.image(img)
    img = np.asarray(img)/255
    img = resize(img,(256,256))
    img = expand_dims(img,axis=0)
    prediction = int(round(model.predict(x=img)).numpy()[0][0])
    prediction = class_indices[prediction]
    return prediction


st.title('Fire Detection from Images')
file = st.file_uploader('Upload Image')
if file is not None:
    try:  
        prediction = predict()
        st.success(f'Prediction: The image contains {prediction}')
    except:
        st.markdown("Error in input file")
