# %% [markdown]

"""
Let's start with the simplest and scrape some key data about one single restaurant.
"""

# %%
import bs4
from bs4 import BeautifulSoup
import requests

# %%
url_restaurant: str = r"https://www.thefork.se/restaurang/trattoria-la-sultana-r67701"
response_restaurant: str = requests.get(url_restaurant, timeout=5).text
soup: BeautifulSoup = BeautifulSoup(response_restaurant, features="lxml")
print(soup.prettify())

# %%
# Start with the resaturant name
name_restaurant: bs4.element.Tag = soup.find(
    "div", class_="styles_gridArea_info__rturB"
)
print(name_restaurant.text)

# Here i run into a problem. The names of the tag I find in
# the browser are rendered with js and not really in the html.
# Scraping the website should be done with Selenium that can
# render the js. But I will not do that here.

# %%
# For now I will just switch to a simpler website. Possibly Wikipedia.

wiki_url: str = r"https://en.wikipedia.org/wiki/2022_FIFA_World_Cup"
wiki_response: requests.models.Response = requests.get(wiki_url, timeout=5)
wiki_text: str = wiki_response.text
wiki_soup: BeautifulSoup = BeautifulSoup(wiki_text, features="lxml")

wiki_title: str = wiki_soup.find("span", class_="mw-page-title-main").get_text()
print(wiki_response)

# Wikipedia was compatible with simple scraping.
# Let's get some more text and work on it.

# %%

wiki_div: BeautifulSoup = wiki_soup.find("div", id="mw-content-text")
wiki_box_text: str = wiki_div.find("div", class_="mbox-text-span").get_text(
    strip=True, separator=" "
)
print(wiki_box_text)
# %%
# We know that the host is Qatar, let's see if we can find it.

wiki_table: BeautifulSoup = wiki_div.find("table", class_="infobox vcalendar").find(
    "tbody" # This is a table body
)
wiki_table_text: str = wiki_table.get_text(strip=True, separator=" ")
print(wiki_table_text)

# Well, sort of, I couldn't find a way to make Qatar distinct from other data in
# the infobox. But that's enough for now.
