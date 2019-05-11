
from bs4 import BeautifulSoup
import requests
from splinter import Browser
import pandas as pd
import requests 


def init_browser(): 
    exec_path = {'executable_path': '/app/.chromedriver/bin/chromedriver'}
    return Browser('chrome', headless=True, **exec_path)

# Create Mission to Mars global dictionary that can be imported into Mongo
mars_info = {}

# NASA MARS NEWS
def scrape_mars_news():
    try: 

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
    finally:

        browser.quit()

# # JPL Mars Space Images - Featured Image
# 
# 
# 


# Visit Mars Space Images through splinter module
jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(jpl_url)


# In[87]:

# FEATURED IMAGE
def scrape_mars_image():

    try: 
        # HTML Object 
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
    finally:

        browser.quit()

# # Mars Weather

def scrape_mars_weather():

    try: 

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
    finally:

        browser.quit()



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



def scrape_mars_hemispheres():

        try: 


            hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
            browser.visit(hemispheres_url)


            # In[104]:


            # HTML Object
            html_hemispheres = browser.html

            # Parse with Beautiful Soup
            soup = BeautifulSoup(html_hemispheres, 'html.parser')

            # get all items that contain mars hemispheres information
            items = soup.find_all('div', class_='item')

            # Create list for hemisphere urls 
            hemisphere_image_urls = []

            # main_url 
            hemispheres_main_url = 'https://astrogeology.usgs.gov'



        # Loop through the items previously stored
        for i in items: 
            # Store title
            title = i.find('h3').text
            
            # Store link to full image website
            partial_img_url = i.find('a', class_='itemLink product-item')['href']
            
            # link that contains the full image website 
            browser.visit(hemispheres_main_url + partial_img_url)
            
            # HTML Object  
            partial_img_html = browser.html
            
            # Parse HTML with Beautiful Soup 
            soup = BeautifulSoup( partial_img_html, 'html.parser')
            
            # Retrieve full image 
            img_url = hemispheres_main_url + soup.find('img', class_='wide-image')['src']
            
            # Append information into a list of dictionaries 
            hemisphere_image_urls.append({"title" : title, "img_url" : img_url})
            

        # Display hemisphere_image_urls
            hemisphere_image_urls

            mars_info['hemisphere_image_urls'] = hemisphere_image_urls

        
            # Return mars_data dictionary 

             return mars_info
    finally:

        browser.quit()


# In[ ]:





# In[ ]:




