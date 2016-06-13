import scrapy

class SongSpider(scrapy.Spider):
    name = "song"
    allowed_domains = ["music.163.com"]
    start_urls = [
        "http://music.163.com/playlist?id=111196540"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)