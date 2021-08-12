# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager

# Import pandas
import pandas as pd

# Set up the executable path (Splinter)
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


### Featured Articles from redplanetscience.com

# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

# Set up the HTML browser
html = browser.html
news_soup = soup(html, 'html.parser')

# Create the parent element
slide_elem = news_soup.select_one('div.list_text')

# Use our parent element to find the title of the article
slide_elem.find('div', class_='content_title')

# Use parent element to find the first 'a' tag and save it as news_title
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# Use parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


### Featured Images from spaceimages-mars.com

# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

# Use the base URL to create an absolute URL for the above image
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


### Mars Facts from galaxyfacts-mars.com

# Create a dataframe from the html table
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()

df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df

# Convert dataframe to html to add to web application
df.to_html()

# End browser activity
browser.quit()



