# %% [Markdown]
COMMENT_1 = """
This py file is used to get data from google's api
There is no need to import any libraries beside requests
to get the desired data from google api. However, some background
work was done:
1. Create a project in google cloud platform.
2. Enable the google api you want to use.
3. Restricted the use of the key to my ip address and to the api I want to use (Places API).
4. For safety I never put the api key in the code. Instead it was stored in .txt file.
   Variable using the terminal.
5. Copy the api key and paste it in the api_key variable.

Also, there are some considerations:
1. Is the language setting important? It can be added &language=LANGUAGE to the query url

2. Use the nearbysearch api to get the data you want
https://maps.googleapis.com/maps/api/place/nearbysearch/json?
    &location=LATITUDE,LONGITUDE
    &radius=RADIUS
    &type=restaurant
    &key=YOUR_API_KEY

3. Alternatively, you can use the textsearch api to get the data you want
https://maps.googleapis.com/maps/api/place/textsearch/json?
    ?query=restaurants%20in%20Sydney
    &key=YOUR_API_KEY
    
4. Data can be extracted in JSON or XML format. The default is JSON, which
is more readable and very similar to Python dictionaries.
"""
print(COMMENT_1)

# %%
# importing libraries here
# pylint: disable=unused-import, wrong-import-position, missing-final-newline
import requests
import pandas as pd
#%%
with open(r'/Users/hashimhabobi/Desktop/Data/google/api_key.txt', 'r', encoding='UTF-8') as f:
    API_KEY: str = f.read()

# %% [markdown]
COMMENT_2 = """
First let's explore if the best option nearbysearch by visualizing a Google map with the
googlemaps library.
"""    
print(COMMENT_2)
# %% 
# configure with the api key
url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query=restauranger%250i%250Göteborg&maxprice=3&type=restaurant&language=sv&key={API_KEY}"

# arguments in the url:
# json: the format of the data (json)
# query: the search query (restauranger i Göteborg)
# maxprice: the maximum price level of the place (3, where 4 is the highest)
# type: the type of place (restaurant)
# language: the language of the place (sv for swedish)

payload = {}
headers = {}

response: requests.models.Response = requests.request("GET", url, headers=headers, data=payload)
df: pd.DataFrame = pd.DataFrame(response.json()['results'])


# %% [markdown]
"""
It wasn't clear that you can only get 20 results at a time. 
It is possible to get more results by adding a pagetoken to the url,
but the limit is still 60 results. Not enough!

There's another API called SERP API that can be used to get more results.
I'm testing that approach instead.
"""

