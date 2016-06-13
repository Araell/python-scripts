from bs4 import BeautifulSoup

source_file = 'echo.html'
source = open(source_file, 'r')


def get_post_name(content):
    soup = BeautifulSoup(content, "lxml")
    return soup.find('div', class_='title fl').h1.text


get_post_name(source.read())
