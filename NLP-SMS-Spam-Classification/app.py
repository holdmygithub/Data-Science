from flask import Flask, render_template, request
import pickle as pkl
from nltk.tokenize import word_tokenize
import re
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import string
import nltk
from scipy.sparse import csr_matrix
import pandas as pd

def get_length(df):
    df = df.apply(len)
    return csr_matrix(df.to_numpy().reshape(-1,1))

def message_cleaner(message):
    cleaned_message = []
    for word in word_tokenize(message.lower()):
        word = re.sub('[^a-zA-Z]','',word)
        if(word == ''):
            continue
        if(word not in remove_list):
            cleaned_message.append(porterstemmer.stem(word))
    return cleaned_message

nltk.download('stopwords')
nltk.download('punkt')

remove_list = set(list(string.punctuation) + stopwords.words('english'))

app = Flask(__name__)
porterstemmer = PorterStemmer()
def message_cleaner(message):
    cleaned_message = []
    for word in word_tokenize(message.lower()):
        word = re.sub('[^a-zA-Z]','',word)
        if(word == ''):
            continue
        if(word not in remove_list):
            cleaned_message.append(porterstemmer.stem(word))
    return cleaned_message

model = pkl.load(open('model.sav','rb'))

print(type(model))
feature_pipe = pkl.load(open('feature_pipe.sav','rb'))
print(type(feature_pipe))

@app.route('/')
def test():
    return render_template('index.html')
@app.route('/submit',methods=["POST"])
def classify():
    text = request.form["text"]
    text = feature_pipe.transform(pd.DataFrame([text],columns=["message"]))
    predict = model.predict(text)
    if(predict == 0):
        predict = 'not spam'
    else:
        predict = 'spam'
    return f"The message is {predict}"

if __name__ == '__main__':
    app.run()
