from bs4 import BeautifulSoup
import requests

with open("website.html", encoding="utf-8") as file:
    contents = file.read()

first_soup = BeautifulSoup(contents, 'html.parser')
# print(soup.title)
# print(soup.prettify())

# Find all of an element
all_anchor_tags = first_soup.find_all(name="a")
# print(all_anchor_tags)

# for tag in all_anchor_tags:
    # print(tag.getText)
    # print(tag.get("href"))

heading = first_soup.find(name="h1", id="name")
# print(heading)

section_heading = first_soup.find(name="h3", class_="heading")
# print(section_heading)

company_url = first_soup.select_one(selector="p a")
name = first_soup.select_one(selector="#name")
# print(name)

headings = first_soup.select(".heading")
# print(headings)

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# article_tag = soup.find(name="a", class_="titlelink")
articles = soup.find_all(name="a", class_="titlelink")
# article_text = article_tag.getText()
# article_link = article_tag.get("href")
# article_upvote = soup.find(name="span", class_="score").getText()

# Find all texts and links connected to each tag
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [score.getText() for score in soup.find_all(name="span", class_="score")]

# print(article_texts)
# print(article_links)
print(article_upvotes[0])
