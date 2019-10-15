import bs4

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>웹 크롤링 실습</title>
    </head>
<body>
    <h1 class="green">1. 웹 크롤링 실습 페이지 입니다.</h1>
    <h1 class="red">2. 웹 크롤링 실습 페이지 입니다.</h1>

    <p>웹 크롤링 실습 p 태그 입니다.</p>
</body>
</html>"""


html_soup = bs4.BeautifulSoup(html, "html.parser")
h1_tag = html_soup.find("h1")
print(h1_tag)
print(h1_tag.text)

html_soup = bs4.BeautifulSoup(html, "html.parser")
h1_tags = html_soup.findAll("h1")
print(h1_tags)
print(h1_tags[0])
print(h1_tags[0].text)

# class가 red인 h1 태그를 찾아보자
html_soup = bs4.BeautifulSoup(html, "html.parser")
h1_tag = html_soup.find("h1", {"class": {"red", "green"}})
print(h1_tag)
print(h1_tag.text)


html_soup = bs4.BeautifulSoup(html, "html.parser")
h1_tags = html_soup.findAll("h1", {"class": {"red", "green"}})
print(h1_tags)
for tag in h1_tags:
    print(tag.text)
