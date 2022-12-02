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
result: requests.models.Response = requests.get(website, timeout = 5)  # pylint: disable=W3101
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
def get_text_from_website(url: str) -> str:
    """_summary_

    Args:
        url (str): _description_

    Returns:
        str: _description_
    """
    response: requests.models.Response = requests.get(url, timeout=5)
    pretty_soup: BeautifulSoup = BeautifulSoup(response.text, "lxml").prettify()
    return pretty_soup


# %%
soup_titanic: str = get_text_from_website(website)
print(soup_titanic)
print(type(soup_titanic))

# %% [markdown]
"""
To get the text from the whole website is easy, and not that useful.
Instead one shoud get the text from a specific section of the website. The tags and elements we
mentioned before.

An idea I want to explore is resaturant in the website: The fork.
"""
# %%
spoton_url: str = r'https://www.thefork.se/restaurang/spoton-restaurang-r384077'
result_spoton: requests.models.Response = requests.get(spoton_url, timeout=5)
content_spoton: str = result_spoton.text
soup_spoton: BeautifulSoup = BeautifulSoup(content_spoton, "lxml")
menu_spoton: bs4.element.Tag = soup_spoton.find("dl", role="presentation")
# %%
print(menu_spoton)
