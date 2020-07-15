import pickle
from flask import Flask, render_template, request
from Templates.forms import SongSubmitForm
app = Flask(__name__)
# app.config['SECRET_KEY'] = 'thecodex'

# Loading the saved XGboost model pickle
# model = open('model.pkl', 'rb')
# model = pickle.load(model)


@app.route('/')
def home():
   return "<h1>Hit Predictor</h1>"

@app.route('/submit')
def submit():
   form = SongSubmitForm()
   return render_template('submission.html', form=form)
   

if __name__ == '__main__':
   app.run(debug=True)

