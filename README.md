# web_scraping

This is a personal project, starting from virtually no specific knowledge of webscraping and aiming to 
know enough to read, parse and structure data from websites in order to analyze it and maybe then create a
model.

## Ideas

1. Restaurant data: Scrape data about all Gothenburg's restaurants in the website the fork and analyze the data
to uncover the most popular restaurants.

## Lessons

1. Not all websites are read the same way in webside and in a request response. Dynamic websites are JS-rendered and tags and classes are not available in the html. In order to get the data, we need to use a headless browser and then parse the html from the browser. This is done using the `selenium` library.
To detect those inspect webiste, go to settings --> debugging --> Disable JS. If website changes or doesn't work it uses JS.

