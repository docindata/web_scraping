# pylint: disable=pointless-string-statement

# %% [markdown]
"""
This is a tutorial on using Selenium

# 1. Intsallation
Chromedriver from Chromium needs to be installed. And pathname needs to be saved.
"""

# %%
import selenium
from selenium import webdriver

# %%
chromdriver_path: str = (
    r"/Applications/chromedriver"  # Path to the executable runs chrome in Selenium.
)

DriverCLass = (
    selenium.webdriver.chrome.webdriver.WebDriver
)  # The driver class for typing

# Now initialize webdrive with chrome
driver: DriverCLass = webdriver.Chrome(
    chromdriver_path
)  # The driver object is created and correctly typed

driver.get("https://www.google.com") # A web page is opened, with a message that chrome is being controlled by automated test software.

# %% [markdown]
"""
An error was encountered when running the chromedriver exectable: “chromedriver” cannot
be opened because the developer cannot be verified.

To fix the issue, the computer needs to trush the application,
so lifting quarantine in terminal was sufficient.
xattr -d com.apple.quarantine /Applications/chromedriver
"""

# %%
driver.quit() # to quit

# %% [markdown]
"""
When using Selenium there are more options to locate element:
1. Using id
2. Using class
3. Using xpath
4. Using css selector
5. Tag name
6. Link text
For example
"""
# %% 