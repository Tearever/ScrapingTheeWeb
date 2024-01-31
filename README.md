# This Project is about Collecting/Scraping News Articles
## The package used to achieve this functionality is [Scrapy](https://scrapy.org/) (v.2.11.0). This is an open-source web crawling and web scraping framework that can be used to extract structured data from websites. 
### The Three main items you need from the repo are the articleScrapper folder, requirements.yaml, and websites.txt. The remaining txt files will be produced on your local machine when we compile the code for the first time.
#### <img src="images/Screenshot%202024-01-29%20182004.png" alt="image of the repo with elements highlighted in yellow"/>
#### requirements.yaml is extremely important since it allows the person who downloaded the file to have the exact environment the developer built the program on top of.  

#### To create a new environment from an yaml file:
```conda create --name (some_name) --file requirement.yaml```
#### or
```conda env create -f requirement.yaml```
#### (This is of course assuming that you already have Miniconda installed on the system)

#### Before jumping into how to pilot scrapy through the command prompt, I would like to introduce you to the concept of spiders. This feature is unique to scrapy and allows a considerable amount of flexibility to our web scraping desires. Each spider has a unique name along with a set of functions. 

#### If you traverse over to [articleScrapper/articleScrapper/spiders/articleSpider.py](https://github.com/Tearever/ScrapingTheeWeb/blob/main/articleScrapper/articleScrapper/spiders/articleSpider.py) you will be greeted by the spider who finished Project 1. 

#### This is articleSpider. You can see his name being defined by this line ```name = "articleSpider"```. As mentioned earlier, these are user-defined and can be named beyond their functionality. 

## 1. Spider Configuration

#### ```name = "articleSpider"``` - This is the name of the spider.
#### ```allowed_domains = ["www.nytimes.com"]``` - It specifies the domain(s) that the spider is allowed to crawl.
#### ```start_urls = open("websites.txt")``` - This file contains a list of URLs that the spider will start crawling.

## 2. Parsing the Response
#### The parse method is called for each URL in the start_urls. It extracts relevant information from the HTML response using CSS selectors. The extracted data includes the article headline, summary, and body.
#### <img src="images/Screenshot%202024-01-30%20194459.png" alt="image showing parse function"/>
