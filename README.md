# web_scraping

This is a personal project, starting from virtually no specific knowledge of webscraping and aiming to 
know enough to read, parse and structure data from websites in order to analyze it and maybe then create a
model.

## Ideas

1. Restaurant data: Scrape data about all Gothenburg's restaurants in the website the fork and analyze the data
to uncover the most popular restaurants.

2. Restaurant data: Use SERP-api to query restaurants in Gothenburg and analyze the data

3. Build a dashboard to share the results of the analysis (Bokeh, Streamlit, Dash, etc.)

## Lessons

1. Not all websites are read the same way in webside and in a request response. Dynamic websites are JS-rendered and tags and classes are not available in the html. In order to get the data, we need to use a headless browser and then parse the html from the browser. This is done using the `selenium` library.
To detect those inspect webiste, go to settings --> debugging --> Disable JS. If website changes or doesn't work it uses JS.

2. Web scraping is not difficult in itself but companies have made it challenging by using bot-detection and adding captchas, there is also the risk for getting your IP blocked from websites such as Google. 

3. Google's Places API was tried and seemed initially like a good tool. However it's not
possible to get more that 60 per query.

## Features

1. Restaurant name
2. Category
3. Price range
4. Rating
5. Address --> Area
6. Number of reviews
7. ... more to come