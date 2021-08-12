# Import dependencies to use flask, render a template, redirect to url and create url. 
# Use pymongo to interact with mongo database
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

# Set up flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Create our home page route
@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)

# Create a route for scraping data from the homepage of our web app
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update({}, mars_data, upsert=True)
   return redirect('/', code=302)

# Tell flask to run
if __name__ == "__main__":
   app.run()