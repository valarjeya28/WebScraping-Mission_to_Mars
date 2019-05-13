# import necessary libraries
from flask import Flask, render_template, redirect
import pymongo
import scrape_mars

# create instance of Flask app
app = Flask(__name__)

# create mongo connection
# setup mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

db = client.mars_db
collection = db.mars_data_entries

@app.route("/")
def home(): 

    # Find data
    mars_info = db.mars_info.find_one()

    # Return template and data
    return render_template("index.html", mars_info=mars_info)

@app.route("/scrape")
def scrape(): 

    # Run scrapped functions
    mars_info = db.mars_info
    mars_data = scrape_mars.scrape_mars_news()
    mars_data = scrape_mars.scrape_mars_image()
    mars_data = scrape_mars.scrape_mars_facts()
    mars_data = scrape_mars.scrape_mars_weather()
    mars_data = scrape_mars.scrape_mars_hemispheres()
    mars_info.update({}, mars_data, upsert=True)

    return redirect("/", code=302)

if __name__ == "__main__": 
    app.run(debug= True)
