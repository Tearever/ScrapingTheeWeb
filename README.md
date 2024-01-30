# This Project is about Collecting/Scrapping News Articles
## The package used to achieve this functionality is Scrapy(v.2.11.0). This is an open-source web crawling and web scraping framework that can be used to extract structured data from websites. 
### The Three main items you need from the repo are the articleScrapper folder, requirements.yaml, and websites.txt. The remaining txt files will be produced on your local machine when we compile the code for the first time.
### <img src="images/Screenshot%202024-01-29%20182004.png" alt="image of the repo with elements highlighted in yellow"/>
### requirements.yaml is extremely important since it allows the person who downloaded the file to have the exact environment the developer built the program on top of.  

### To create a new environment from an yaml file:
```conda create --name (some_name) --file requirement.yaml```
### or
```conda env create -f requirement.yaml```
#### (This is of course assuming that you already have Miniconda installed on the system)

## Before jumping into how to pilot scrapy through the command prompt, I would like to introduce you to the concept of spiders. This feature is unique to scrapy and allows a considerable amount of flexibility to our web scrapping desires. Each spider has a unique name along with a set of functions. 
