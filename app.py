import flask
from flask import Flask, render_template, request
from spotify_api.fetch_data import *
app = Flask(__name__)
app.config['SECRET_KEY'] = 'thecodex'


@app.route('/', methods=["POST"])
def home():
   if request.form:
      title = request.form['song_title']
      artist = request.form['artist_name']
      predictions = make_prediction(str(title), str(artist))
      render_template('submission.html', prediction=predictions)
      
   return predictions

   

if __name__ == '__main__':
   app.run(debug=True)

