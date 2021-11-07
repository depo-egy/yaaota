import flask
from flask import Flask, jsonify, request
import joblib
from sklearn.feature_extraction.text import CountVectorizer


model = joblib.load('finalized_model.sav')
app = Flask(__name__)

cv_model =  joblib.load("cv.pkl")


@app.route('/api/get_category', methods=['GET'])
def get_category():
    cv = CountVectorizer()
    title = request.args.get('title')
    category = model.predict(cv_model.transform([title]))
    return jsonify({'category': str(category)})
    #return jsonify("hello")



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
