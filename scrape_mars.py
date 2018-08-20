
from splinter import Browser
from bs4 import BeautifulSoup

import time
import pandas as pd

def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    return browser = Browser('chrome', **executable_path, headless=False)

def mars_news_function():
    browser = init_browser()

    url_Mars_news = "https://mars.nasa.gov/news/"

    browser.visit(url_Mars_news)
    time.sleep(1)

    html = browser.html

    soup = BeautifulSoup(html, 'html.parser')


    article_heading_list = []

    for article_heading in soup.find_all('div', class_="content_title"):
        article_heading_list.append(article_heading.find('a').text)


    article_details_list = []
    for article_details in soup.find_all('div', class_="article_teaser_body"):
        article_details_list.append(article_details.text)


    latest_news_title = article_heading_list[0]

    latest_news_details = article_details_list[0]

    news_dict = {"Headline": latest_news_title, "Details": latest_news_details}

    return news_dict

def feature_image_function():
    browser = init_browser()

    url_mars_space_images = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"

    browser.visit(url_mars_space_images)
    time.sleep(1)

    html = browser.html

    soup = BeautifulSoup(html, 'html.parser')


    featured_image_list = []
    for image in soup.find_all('div', class_="img"):
        featured_image_list.append(image.find('img').get('src'))


    feature_image = featured_image_list[0]

    feature_image_url = "https://www.jpl.nasa.gov/" + feature_image

    feature_image_dict = {"image": feature_image_url}

    return feature_image_dict

def Weather_function():
    browser = init_browser()

    url_mars_weather = "https://twitter.com/marswxreport?lang=en"

    browser.visit(url_mars_weather)
    time.sleep(1)

    html = browser.html

    soup = BeautifulSoup(html, 'html.parser')


    weather_info_list = []

    for weather_info in soup.find_all('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"):
        weather_info_list.append(weather_info.text)


    latest_mars_weather = weather_info_list[0]

    mars_weather_dict = {"mar_weather": latest_mars_weather }

    return mars_weather_dict
    
def mars_facts_table_function():
    browser = init_browser()

    df_mars_facts = pd.read_html("https://space-facts.com/mars")

    df_mars_facts = df_mars_facts[0]

    df_mars_facts.rename_axis({0:"Parameters", 1:"Values"},axis=1, inplace=True)

    df_mars_facts_table = df_mars_facts.to_html("df_mars_facts_table.html", index=False)


    df_mars_facts_dict = {"df_mars_facts": df_mars_facts_table}

    return df_mars_facts_dict


def hemisphere_images():
    image_one = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'
    image_two = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'
    image_three = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'
    image_four = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'

    full_hemisphere_dict = {"image_one": image_one, "image_two":image_two, "image_three":image_three, "image_four":image_four}

    return full_hemisphere_dict

