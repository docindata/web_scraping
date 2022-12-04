# pylint: disable=W0105:pointless-string-statement
# %% [markdown]
"""
Starting with a simple py.file
"""
# %%
import requests
import bs4  # type: ignore
from bs4 import BeautifulSoup  # type: ignore

## %% [markdown]
"""
Now lets get HTML from a website with Titanic
"""
# %%
website: str = r"https://subslikescript.com/movie/Titanic-120338"
result: requests.models.Response = requests.get(
    website, timeout=5
)  # pylint: disable=W3101
soup: BeautifulSoup = BeautifulSoup(result.text, "lxml")
"""
finding elements with a recommended order
# 1. ID
# 2. Class name
# 3. Tag name, CSS selector
# 4. Xpath
"""
box: bs4.element.Tag = soup.find(
    "article", class_="main-article"
)  # Simply locating the section
# %%
def get_text_from_website(url: str, timeout: int = 5) -> str:
    """_summary_

    Args:
        url (str): _description_

    Returns:
        str: _description_
    """
    response: requests.models.Response = requests.get(url, timeout=timeout)
    pretty_soup: BeautifulSoup = BeautifulSoup(response.text, "lxml").prettify()
    return pretty_soup


# %%
soup_titanic_1: str = get_text_from_website(website)
print(soup_titanic_1)
print(type(soup_titanic_1))

# %% [markdown]
"""
To get the text from the whole website is easy, and not that useful.
Instead one shoud get the text from a specific section of the website. The tags and elements we
mentioned before.

An idea I want to explore is resaturant in the website: The fork.
"""
# %%
titanic_url: str = r"https://subslikescript.com/movie/Titanic-120338"
result_titanic: requests.models.Response = requests.get(titanic_url, timeout=5)
content_titanic: str = result_titanic.text
soup_titanic: BeautifulSoup = BeautifulSoup(content_titanic, "lxml")
menu_titanic: bs4.element.Tag = soup_titanic.find("article", class_="main-article")
print(menu_titanic)

# %%
title_titanic: str = menu_titanic.find("h1").get_text()
print(title_titanic)
# %%
transcript_titanic: str = menu_titanic.find("div", class_="full-script").get_text()
print(transcript_titanic)
# To put spaces between the lines we can add a couple of params in the get_text() method

# strip: Bool. Removes trailing and preceeding spaces in lines
# seperator: str. Add space between words from different lines.
transcript_titanic: str = menu_titanic.find("div", class_="full-script").get_text(  # type: ignore
    strip=True, separator=" "
)
print(transcript_titanic)
