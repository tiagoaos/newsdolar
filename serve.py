mport pandas as pd
import numpy as np
from sklearn.naive_bayes import MultinomialNB, ComplementNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn import svm
from sklearn.metrics import confusion_matrix, f1_score, classification_report, accuracy_score, roc_curve, auc
from sklearn.model_selection import train_test_split
#from sklearn.externals import joblib
import matplotlib.pyplot as plt
import seaborn as sns
#import texthero as hero
from datetime import datetime
from nltk.corpus import stopwords
import nltk
from flask import Flask
app = Flask(__name__)
@app.route("/")

def hello():
    return "Hello World!"
from flask import make_response, jsonify


stock = {
    "fruit": {
        "apple": 30,
        "banana": 45,
        "cherry": 1000
    }
}


df = pd.read_csv('noticias1.csv',header=None, sep='\n')
df2 = pd.read_csv('noticias2.csv',header=None, sep='\n')
df4 = pd.read_csv('noticias3.csv',header=None, sep='\n')


frames = [df, df2, df3]
pd_text = pd.concat(frames)
pd_text.rename(columns = {"published_at": "date"},inplace=True)
# Transforma a string em data mantendo somente a data
pd_text['date'] = pd.to_datetime(pd_text['date'], format='%Y-%m-%d')
pd_text['date2'] = pd_text['date'].dt.normalize()
pd_text.head(5)


# @app.route("/stock")
# def get_stock():
#     res = make_response(jsonify(stock), 200)
#     return res




# if __name__ == "__main__":
#     app.run(port=80,host='0.0.0.0')