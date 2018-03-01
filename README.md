# Web crawling with scrapy python

Web Scraping for marvel all time movies from [Marvel](https://marvel.com/movies/all)

## Getting Started

Scrapy is an application framework for crawling web sites and extracting structured data which can be used for a wide range of useful applications, like data mining, information processing or historical archival.

## Installing

[scrapy installation](https://doc.scrapy.org/en/latest/intro/install.html)


## Creating a project

	scrapy startproject tutorial
above commands will create a following folders and files
```
	  tutorial/
	    scrapy.cfg            # deploy configuration file
	    tutorial/             # project's Python module, you'll import your code from here
	        __init__.py
        items.py          # project items definition file
        middlewares.py    # project middlewares file
        pipelines.py      # project pipelines file
        settings.py       # project settings file
        spiders/          # a directory where you'll later put your spiders
            __init__.py
            *** add "marvel_spider.py" in side spiders folder
```


## class & tegs 

    <div class="row-item-text">
        <p class="movie-disposition upcoming">Upcoming</p>
        <h5><a  class="meta-title" href="/movies/movie/225/captain_marvel">Captain Marvel</a></h5>
        <p class="media-item-meta">Mar 8, 2019</p>
	</div>

## Data Extraction
	
using [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.html?highlight=select) to Extract required fields.

```
BeautifulSoup(response.body, "lxml")
```

## Runing spider and write data to csv file 
	scrapy crawl marvel_spider -o marvel_movies.csv
