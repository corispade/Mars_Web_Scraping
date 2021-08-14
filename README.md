# Mission to Mars Web Scraping

# Overview

Utilizing BeautifulSoup and Splinter to scrape data from websites to retrieve news about Mars, facts about Mars, space images from Mars, and images of Mars hemispheres. We are storing the scraped data into a Mongo database and using a Flask web application to display the data. 

## Process:

### Deliverable 1: Scrape Full-Resolution Mars Hemisphere Images and Titles
Find scraping code [here](https://github.com/corispade/Mission_to_Mars/blob/main/Mission_to_Mars_Challenge.ipynb).

1. Created a function that retrieved full-resolution image and title from each Mars hemisphere
2. Added the full-resolution images and titles to a dictionary
3. Created a list to hold the dictionary containing the above data

### Deliverable 2: Update the Web App with Mars Hemisphere Images and Titles

1. Added our Deliverable 1 scraping code to [scraping.py](https://github.com/corispade/Mission_to_Mars/blob/main/scraping.py) file
2. Updated the Mongo database to contain our hemisphere dictionary
3. Created [index.html](https://github.com/corispade/Mission_to_Mars/blob/main/templates/index.html) file to format and display the data using [Flask](https://github.com/corispade/Mission_to_Mars/blob/main/app.py)

### Deliverable 3: Add Bootstrap 3 Components
1. Made the webpage mobile responsive
2. Added components to style the webpage

## Resources:
Data Sources: 
* [Mars News](https://redplanetscience.com)
* [Featured Image](https://spaceimages-mars.com)
* [Mars Facts](https://galaxyfacts-mars.com)
* [Mars Hemispheres](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars)

Versions: Python 3.7.6, Conda 4.10.1, HTML5

Environment: Jupyter Notebook, Visual Studio Code

# Webpage Results:

![image](https://github.com/corispade/Mission_to_Mars/blob/main/references/webpage%201.png) ![image](https://github.com/corispade/Mission_to_Mars/blob/main/references/webpage%202.png)


# Summary:
This webpage will continue to scrape the newest data from each of these websites. We will be able to use it to keep up to date with news and developments on Mars.
