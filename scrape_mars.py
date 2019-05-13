from bs4 import BeautifulSoup
import requests
from splinter import Browser
import pandas as pd
import requests 



def init_browser(): 
    exec_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser('chrome', headless=True, **exec_path)


mars_info = {}

# NASA MARS NEWS
def scrape_mars_news():
    
        # Initialize browser 
        browser = init_browser()

        # URL of page to be scraped
        url = 'https://mars.nasa.gov/news/'


        browser.visit(url)

        # HTML Object
        html = browser.html

        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html, 'html.parser')


        # Retrieve the latest element that contains news title and news_paragraph
        news_title = soup.find('div', class_='content_title').find('a').text
        news_p = soup.find('div', class_='article_teaser_body').text
        # Dictionary entry from MARS NEWS
        mars_info['news_title'] = news_title
        mars_info['news_paragraph'] = news_p

        return mars_info
    

# # JPL Mars Space Images - Featured Image
# 
# 
# 
# FEATURED IMAGE
def scrape_mars_image():

    
        # Initialize browser 
        browser = init_browser()

        #browser.is_element_present_by_css("img.jpg", wait_time=1)

        # Visit Mars Space Images through splinter module
        image_url_featured = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
        browser.visit(image_url_featured)# Visit Mars Space Images through splinter module

        html_image = browser.html

        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html_image, 'html.parser')

        # Retrieve background-image url from style tag 
        featured_image_url  = soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]

        # Website Url 
        main_url = 'https://www.jpl.nasa.gov'

        # url with scrapped route
        featured_image_url = main_url + featured_image_url

        # Display full link to featured image
        featured_image_url
         # Dictionary entry from FEATURED IMAGE
        mars_info['featured_image_url'] = featured_image_url 
        
        return mars_info
    

# # Mars Weather

def scrape_mars_weather():

    

        # Initialize browser 
        browser = init_browser()

        twitter_url="https://twitter.com/marswxreport?lang=en"

        browser.visit(twitter_url)



        # HTML Object 
        html_image = browser.html

        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html_image, 'html.parser')


        #get the weather tweet
        latest_tweets = soup.find('p', class_='TweetTextSize').text
        #latest_tweets
        mars_info['weather_tweet'] = latest_tweets
        
        return mars_info
    


# # Mars Facts
def scrape_mars_facts():


            facts_url = "https://space-facts.com/mars/"


            mars_facts = pd.read_html(facts_url)
            mars_facts
            mars_df = mars_facts[0]

            # Assign the columns
            mars_df.columns = ['Description','Value']

            #mars_df.set_index('Description', inplace=True)

            # Save html code 
            mars_df.to_html()

            data = mars_df.to_dict(orient='records') 

            
                # Dictionary entry from MARS FACTS
            mars_info['mars_facts'] = data

            return mars_info



# MARS HEMISPHERES


def scrape_mars_hemispheres():
 

        # Initialize browser 
        browser = init_browser()

        # Visit hemispheres website through splinter module 
        hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
        browser.visit(hemispheres_url)

        # HTML Object
        html_hemispheres = browser.html

        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html_hemispheres, 'html.parser')

        # Retreive all items that contain mars hemispheres information
        items = soup.find_all('div', class_='item')

        # Create empty list for hemisphere urls 
        hiu = []

        # Store the main_ul 
        hemispheres_main_url = 'https://astrogeology.usgs.gov' 

        # Loop through the items previously stored
        for i in items: 
            # Store title
            title = i.find('h3').text
            
            # Store link that leads to full image website
            partial_img_url = i.find('a', class_='itemLink product-item')['href']
            
            # Visit the link that contains the full image website 
            browser.visit(hemispheres_main_url + partial_img_url)
            
            # HTML Object of individual hemisphere information website 
            partial_img_html = browser.html
            
            # Parse HTML with Beautiful Soup for every individual hemisphere information website 
            soup = BeautifulSoup( partial_img_html, 'html.parser')
            
            # Retrieve full image source 
            img_url = hemispheres_main_url + soup.find('img', class_='wide-image')['src']
            
            # Append the retreived information into a list of dictionaries 
            hiu.append({"title" : title, "img_url" : img_url})

        mars_info['hiu'] = hiu

        
        # Return mars_data dictionary 

        return mars_info
    
