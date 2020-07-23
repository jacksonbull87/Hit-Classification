import flask
from flask import Flask, render_template, request
from spotify_api.fetch_data import *
app = Flask(__name__)
app.config['SECRET_KEY'] = 'thecodex'


@app.route('/', methods=["GET"])
def home():
   return render_template('index.html')

@app.route('/', methods=["GET", "POST"])
def predict():
   title = request.form['song_title']
   artist = request.form['artist_name']
   output = make_prediction(title, artist)
   
   return render_template('prediction.html', prediction=output)



if __name__ == '__main__':
   app.run(host='0.0.0.0')

