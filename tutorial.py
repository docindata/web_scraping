# %% [markdown]
"""
Starting with a simple py.file
"""
# %%
import requests
import bs4 # type: ignore
from bs4 import BeautifulSoup # type: ignore
# %%
result_prem: requests.models.Response = requests.get( # pylint: disable=W3101
    "https://www.google.com"
)
content_prem: str = result_prem.text
soup_prem: BeautifulSoup = BeautifulSoup(content_prem, "lxml")
# %%
print(soup_prem.prettify()) # This method makes the HTML readable
# %%
# Finding tags in the HTML can be done with the find method
print(soup_prem.find('a', class_ = 'gb1'))
# The args are the tag name and the class name. More on tag names in Miro
# %%
# find_all repeats the find method for all the tags in the HTML
print(soup_prem.find_all('a'))
# %% [markdown]
# Now lets get HTML from a website with Titanic
# %%
website: str = r'https://subslikescript.com/movie/Titanic-120338'
result: requests.models.Response = requests.get(website) # pylint: disable=W3101
soup: BeautifulSoup = BeautifulSoup(result.text, "lxml")
# finding elements with a recommended order
# 1. ID
# 2. Class name
# 3. Tag name, CSS selector
# 4. Xpath
box: bs4.element.Tag = soup.find('article', class_='main-article') # Simply locating the section
# %%
