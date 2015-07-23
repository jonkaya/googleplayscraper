####========================
###Sample Scraper for Google Play Top Free Apps
####========================

A project for scraping top 500 free apps on Google Play using scrapy and store on MongoDB.

To use this project follow these steps:

. Create your working environment
. Clone project
. Installation of Dependencies
. Running Project

####Working Environment

```bash
    $ mkvirtualenv scraper
    $ workon scraper
```


####Cloning project

```bash
    $ git clone https://github.com/asimcan/googleplayscraper
```

####Installation of Dependencies
In development:

```bash
    $ pip install -r requirements/dev.txt
```

In production:

```bash
    $ pip install -r requirements/prod.txt
```

####Running Project

```bash
    (scraper)$ python main.py --init
```

This will create scheduled jobs using Advanced Python Scheduler and crawl the website once every hour.
