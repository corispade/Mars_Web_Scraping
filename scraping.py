# Import Dependencies
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt
from webdriver_manager.chrome import ChromeDriverManager

# add function to initalize the browser, create a data dictionary, end webdriver and return scraped data
def scrape_all():

    # Initiate headless driver for deployment
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    # Set news title and news paragraph variables
    news_title, news_paragraph = mars_news(browser)

    # Run all scraping functions and store results in dictionary
    data = {
      "news_title": news_title,
      "news_paragraph": news_paragraph,
      "featured_image": featured_image(browser),
      "facts": mars_facts(),
      "last_modified": dt.datetime.now(),
      "hemispheres": mars_hemispheres(browser)
    }

    # Stop webdriver and return data
    browser.quit()
    return data

### Featured Articles from redplanetscience.com

# Create a function to reuse code
def mars_news(browser):

    # Visit the mars nasa news site
    url = 'https://redplanetscience.com'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    # Set up the HTML browser
    html = browser.html
    news_soup = soup(html, 'html.parser')

    # Add try/except clause for error handling
    try: 
       # Create the parent element
       slide_elem = news_soup.select_one('div.list_text')

       # Use parent element to find the first 'a' tag and save it as news_title
       news_title = slide_elem.find('div', class_='content_title').get_text()

       # Use parent element to find the paragraph text
       news_p = slide_elem.find('div', class_='article_teaser_body').get_text()

    except AttributeError:
        return None, None

    return news_title, news_p


### Featured Images from spaceimages-mars.com

# Create a function to reuse code
def featured_image(browser): 

    # Visit URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # Add try/except clause for error handling
    try: 

    # Find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    except AttributeError:
       return None   

    # Use the base URL to create an absolute URL for the above image
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'

    return img_url


### Mars Facts from galaxyfacts-mars.com

def mars_facts():
 
    # Add try/except clause for error handling
    try:

       # use 'read_html" to scrape the facts table into a dataframe
       df = pd.read_html('https://galaxyfacts-mars.com')[0]
       
    except BaseException:
       return None

    # assign columns and set index of dataframe
    df.columns=['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace=True)

    return df.to_html()

### Scrape High-Resolution Mars’ Hemisphere Images and Titles

def mars_hemispheres(browser):

    # 1. Use browser to visit the URL 
    #url = 'https://marshemispheres.com/'
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    # Parse the html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # Create a parent element to retrieve image urls and titles
    hemisphere_links = img_soup.find_all('div', class_="item")

    # 2. Create a list to hold the images and titles.
    hemisphere_image_urls = []

    # Set up parent url
    parent_url = 'https://astrogeology.usgs.gov'

    # 3. Write code to retrieve the image urls and titles for each hemisphere.
    for link in hemisphere_links:

        # Find the title
        title = link.find('h3').text
        #print(title)
        
        # Find thumbnail image links
        thumb_img = link.find('a', class_='itemLink product-item')['href']
        
        # Click on thumbnail image link
        ##updated to parent url       
        browser.visit(parent_url + thumb_img)
        
        # Create new html from the thumbnail image link
        thumb_img_html = browser.html
        
        # Parse the new html with soup
        thumb_img_soup = soup(thumb_img_html, 'html.parser')

         ## removed url +          
        # Find full image url
        img_url = parent_url + thumb_img_soup.find('img', class_='wide-image').get('src')
        
        # Create a dictionary to store titles and image urls
        hemispheres = {'image_url' : img_url, 'title' : title}
        #hemisphere_image_urls.append({'image_url' : img_url, 'title' : title})
        
        # Add hemispheres dictionary to hemisphere image url list
        hemisphere_image_urls.append(hemispheres)

    # 4. Print the list that holds the dictionary of each image url and title.
    return hemisphere_image_urls


if __name__ == "__main__":

    # If running as script, print scraped data
    print(scrape_all())



