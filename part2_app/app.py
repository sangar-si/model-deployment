import numpy as np 
import flask
from flask import Flask, request, make_response, jsonify
from datetime import datetime
from transformers import AutoModelForSequenceClassification
from transformers import TFAutoModelForSequenceClassification
from transformers import AutoTokenizer
from scipy.special import softmax
import csv
import urllib.request

app = Flask(__name__)

task='sentiment'
MODEL = f"cardiffnlp/twitter-roberta-base-{task}"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL)
model.save_pretrained(MODEL)
tokenizer.save_pretrained(MODEL)

def preprocess(text):
    new_text = []
    # text = text.replace("+"," ")
    for t in text.split("+"):
        t = '@user' if t.startswith('@') and len(t) > 1 else t
        t = 'http' if t.startswith('http') else t
        new_text.append(t)
    return " ".join(new_text)

@app.route('/')
def get_senti():
    try:
        text = request.args['text']
    except:
        return flask.jsonify({"Positive":None, "Negative":None, "Neutral":None})
    task='sentiment'
    MODEL = f"cardiffnlp/twitter-roberta-base-{task}"
    labels=['negative', 'neutral', 'positive']
    text = preprocess(text)
    try:
        text = tokenizer(text, return_tensors='pt')
        output = model(**text)
    except:
        # tokenizer = AutoTokenizer.from_pretrained(MODEL)
        # model = AutoModelForSequenceClassification.from_pretrained(MODEL)
        # model.save_pretrained(MODEL)
        # tokenizer.save_pretrained(MODEL)
        # text = tokenizer(text, return_tensors='pt')
        # output = model(**text)
        pass
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)
    ranking = np.argsort(scores)
    ranking = ranking[::-1]
    resp = {labels[ranking[i]]:np.round(float(scores[ranking[i]]),4) for i in range(scores.shape[0])}
    return flask.jsonify(resp)

if __name__ == "__main__":
    task='sentiment'
    MODEL = f"cardiffnlp/twitter-roberta-base-{task}"
    tokenizer = AutoTokenizer.from_pretrained(MODEL)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL)
    model.save_pretrained(MODEL)
    tokenizer.save_pretrained(MODEL)
    print("Inference app ready...")
    app.run(host="localhost", port = 7050, debug=True)

    
