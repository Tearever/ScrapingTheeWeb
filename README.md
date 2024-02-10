# This Project is about Collecting/Scraping News Articles
## The package used to achieve this functionality is [Scrapy](https://scrapy.org/) (v.2.11.0). This is an open-source web crawling and web scraping framework that can be used to extract structured data from websites. 
#### The Three main items you need from the repo are the articleScrapper folder, requirements.yaml, and websites.txt. The remaining txt files will be produced on your local machine when we compile the code for the first time.
#### <img src="images/Screenshot%202024-01-29%20182004.png" alt="image of the repo with elements highlighted in yellow"/>
#### requirements.yaml is extremely important since it allows the person who downloaded the file to have the exact environment the developer built the program on top of.  

## To create a new environment from an yaml file:
```conda create --name some_name --file requirement.yaml```
#### or
```conda env create -f requirement.yaml```
#### (This is of course assuming that you already have Miniconda installed on the system)

#### Before jumping into how to pilot scrapy I would like to introduce you to the concept of spiders. This feature is unique to scrapy and allows a considerable amount of flexibility to our web scraping desires. Each spider has a unique name along with a set of functions. 

#### If you traverse over to [articleScrapper/articleScrapper/spiders/articleSpider.py](https://github.com/Tearever/ScrapingTheeWeb/blob/main/articleScrapper/articleScrapper/spiders/articleSpider.py) you will be greeted by the spider who finished Project 1. 

## 1. Spider Configuration

#### ```name = "articleSpider"``` - This is the name of the spider.
#### ```allowed_domains = ["www.nytimes.com"]``` - It specifies the domain(s) that the spider is allowed to crawl.
#### ```start_urls = open("websites.txt")``` - This file contains a list of URLs that the spider will start crawling.

## 2. Parsing the Response
#### The parse method is called for each URL in the start_urls. It extracts relevant information from the HTML response using CSS selectors. For instance, in this image, our Spider is looking for an h1 tag that contains a data-testid that is equal to "headline". If the spider finds it, it will only take the ::text from it. The content is then stored in a variable named headline. 
#### <img src="images/Screenshot%202024-01-30%20194459.png" alt="image showing parse function"/>

## 3. Saving to Text File
#### The save_to_text_file method is responsible for saving the extracted information to a text file. The filename is generated based on the first 10 characters of the article's headline, and the content includes the headline, summary, and the article body.
#### <img src="images/Screenshot%202024-01-30%20195110.png" alt="image showing save_to_text_file function"/>

## How to use:
#### 1. Make sure to activate the conda environment made by the requirement.yaml file, ```conda activate some_name```
#### 2. Use ```conda list``` and look for the scrapy package to double check to see if it is installed. If not you can simply use, ```pip install scrapy```.
#### 3. Navigate over to the articleScrapper directory through command line interface (Terminal - mac, Command Prompt - Windows) . You need the parent directory, so please make sure you are not in the sub directory named articleScrapper. Check by using ```dir``` or ```ls```, there should be two items listed: a folder named articleSpider and scrapy.cfg
#### <img src="images/Screenshot%202024-02-10%20154936.png" alt="image of correct directoy in command line interface"/>
#### 4. If everything seems in check try using ```scrapy crawl articleSpider```. If everything is setup properly this should generate five text files with data from each article
