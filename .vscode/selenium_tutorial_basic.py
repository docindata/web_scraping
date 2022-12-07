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

driver.get(
    "https://www.google.com"
)  # Crome opens, message: chrome is being controlled by automated test software.

# %% [markdown]
"""
An error was encountered when running the chromedriver exectable: “chromedriver” cannot
be opened because the developer cannot be verified.

To fix the issue, the computer needs to trush the application,
so lifting quarantine in terminal was sufficient.
xattr -d com.apple.quarantine /Applications/chromedriver
"""

# %%
driver.quit()  # to quit

# %% [markdown]
"""
When using Selenium there are more options to locate element:
1. Using id: driver.find_element_by_id("id")
2. Using class: driver.find_element_by_class_name("class")
3. Using xpath: driver.find_element_by_xpath("//div[@class='class']")
4. Using css selector: driver.find_element_by_css_selector("div.class")
5. Tag name: driver.find_element_by_tag_name("div")
6. Link text: driver.find_element_by_link_text("link text")

All the above can be done itertively by using find_elements instead of find_element.
"""

# %%
driver: DriverCLass = webdriver.Chrome(chromdriver_path)

website_thefork: str = r"https://www.thefork.se/restaurang/trattoria-la-sultana-r67701"
xpath = r"//h1[@class='css-md0073 e7dhrrp0']"  # Selects restaurant name
driver.get(website_thefork)


driver.find_element_by_xpath(xpath)

# Problem: The fork has blocked scraping. There is a captcha to solve,
# making this approach obsolete. Most of the projects I'm interested in
# are made impossible due to this. Using APIs such as SERPapi save so much
# time that any other approach is time consuming.
# One path to explore is Scraping Google-maps

# q: Is scraping google maps possible?
# a: Yes, but it is not easy. Google maps is a single page application

# q: What is a single page application
# a: A single page application is a web application or web site that fits on
# a single web page with the goal of providing a more fluid user experience
# akin to a desktop application. In a single page application, either all
# necessary code – HTML, JavaScript, and CSS – is retrieved with a single page
# load, or the appropriate resources are dynamically loaded and added to the page
# as necessary, usually in response to user actions. The page does not reload at any
# point in the process, nor does control transfer to another page, although the location
# hash or the HTML5 History API can be used to provide the perception and
# navigability of separate logical pages in the application.


