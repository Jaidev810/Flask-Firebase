from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import firebase_database


app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        dealer = request.form['dealer']
        rating = request.form['rating']
        comments = request.form['comments']

        if customer == '' or dealer == '':
            return render_template("index.html", message='Please enter required fields')
        
        #creating and pushing data to firebase
        obj = firebase_database.FirebaseData()
        obj.Set(customer, {"Dealer" : dealer, "Rating" : rating, "Comments" : comments})
        return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)