###========================
###Sample Scraper for Google Play Top Free Apps
###========================

A project for scraping top 500 free apps on Google Play and store on a local Sqlite database.

To use this project follow these steps:

. Create your working environment
. Clone project
. Install additional dependencies
. Running Project
. Run Scraper

###Working Environment
###===================

```bash
    $ mkvirtualenv scraper
    $ workon scraper
```


###Cloning project
###=====================

```bash
    $ git clone https://github.com/asimcan/googleplayscraper
```

###Installation of Dependencies
###=============================

In development::

```bash
    $ pip install -r requirements/local.txt
```

###Running Project
###=============================

```bash
    (scraper)$ python manage.py syncdb
    (scraper)$ python manage.py runserver --settings=APP.settings.local
```


###Running Scraper
###=============================

in local browser proceed to
```bash
    http://localhost:8000/startgoogleplayscraper/
```

This webpage will trigger scraper thread and crawl found web pages.

```bash
    http://localhost:8000/googleplaytopfreeappslist/
```

contains a table for listing crawled content