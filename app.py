import flask
from flask import Flask, render_template, request
from spotify_api.fetch_data import *
app = Flask(__name__)
app.config['SECRET_KEY'] = 'thecodex'


@app.route('/')
def home():
   return render_template('submission.html')

@app.route('/', methods=["GET", "POST"])
def predict():
   if request.form:
      title = request.form['song_title']
      artist = request.form['artist_name']
      output = make_prediction(str(title), str(artist))
      
      
   return render_template('submission.html', prediction=output)

   

if __name__ == '__main__':
   app.run(debug=True)

