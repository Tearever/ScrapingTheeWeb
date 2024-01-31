import scrapy


class ArticlespiderSpider(scrapy.Spider):
    name = "articleSpider"
    allowed_domains = ["www.nytimes.com"]
    start_urls = open("..\websites.txt", "r")

    def parse(self, response):
        headline = response.css('h1[data-testid="headline"]::text').get()
        summary = response.css('p#article-summary::text').get()
        body = response.css('section[name="articleBody"] ::text').getall()

        self.save_to_text_file(headline, summary, body)

    def save_to_text_file(self, headline, summary, body):
        filename = f"..\{headline[:10]}.txt"

        with open(filename, "w", encoding="utf-8") as file:
            file.write(f"Headline: {headline}\n\n")
            file.write(f"Summary: {summary}\n\n")
            file.write("Body:")
            for paragraph in body:
                file.write(f"{paragraph[:200]}")
            