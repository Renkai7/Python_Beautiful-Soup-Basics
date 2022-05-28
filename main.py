from bs4 import BeautifulSoup
import requests

with open("website.html", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
# print(soup.title)
# print(soup.prettify())

# Find all of an element
all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# for tag in all_anchor_tags:
    # print(tag.getText)
    # print(tag.get("href"))

heading = soup.find(name="h1", id="name")
# print(heading)

section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)

company_url = soup.select_one(selector="p a")
name = soup.select_one(selector="#name")
# print(name)
#
headings = soup.select(".heading")
# print(headings)

response = requests.get("https://news.ycombinator.com/news")
print(response.text)
