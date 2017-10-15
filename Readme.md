## TVTropes scraper

### General info

(This project is currently in the process of being cleaned up whenever I have spare time.)

Short version:

This can (kind of) predict what's going to happen next in TV shows, movies, books, webcomics, and other various media. Continue reading to find out how!

Not actually that long version:

This isn't just a webscraper for [TVTropes](http://tvtropes.org/) (fair warning, following TVTropes links is a bit like going down the rabbit hole: you will discover a strange, marvelous place where you might get lost forever), it's also a recommender system that processes the data it gets from TVTropes and uses it to predict the tropes a work is going to use next. 

I started this project for a data mining class I was taking the spring of 2016, and there's still some more work I'd like to do on it, to improve the predictions it gives, but it's functional and gives good predictions, as far as I can tell. 

---

### Dependencies

##### Required:

- Python 2.7.11
- Scrapy 1.0.5
- SciPy 0.13.3
- Graphlab 1.9

##### Optional:
- Numba 0.25.0 
(I used numba's autojit compiler to speed up the recommender. Even with autojit it can take a couple hours, depending on the size of the dataset and which solver you're using.)

### How it works

#### Scraper

The scraper was made using [Scrapy](http://scrapy.org/) and the majority of it resides in tvtropes/tvtropes. The important/interesting part that actually gets the data I want from the html responses is [tvtropes_spider.py](https://github.com/annajo1138/tvtropes_scraper/blob/master/tvtropes/tvtropes/spiders/tvtropes_spider.py). The scraper can be run using the docrawl.sh bash script (just change the file name, jobdir, and nice value to suit your purposes). You can pause the crawl at any time by doing ctrl-C and waiting for it to finish whatever it was doing and restart by running the script again. For more info, the [Scrapy docs](http://scrapy.org/doc/) are very helpful.

It outputs a JSON file containing the following keys for each page:

- title - the name displayed on the page
- all_links - every internal link in the main content
- url_name - the name of the page from the url
- namespace - the section of the site TVTropes considers the page to be in
- pageType - whether the page is for a work, trope, or creator

#### Processing JSON

