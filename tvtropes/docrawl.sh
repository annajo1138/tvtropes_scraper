#!/bin/bash

nice -n 10 scrapy crawl -o tropes_20-06-2016.json -s JOBDIR=crawls/tvtropes-5 tvtropes
