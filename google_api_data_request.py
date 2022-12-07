# %% [Markdown]
COMMENT_1 = """
This py file is used to get data from google's api
There is no need to import any libraries beside requests
to get the desired data from google api. However, some background
work was done:
1. Create a project in google cloud platform.
2. Enable the google api you want to use.
3. Restricted the use of the key to my ip address and to the api I want to use (Places API).
4. For safety I never put the api key in the code. Instead it was stored as an environment
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
# pylint: disable=unused-import, wrong-import-position
import requests

#%%

# %%
