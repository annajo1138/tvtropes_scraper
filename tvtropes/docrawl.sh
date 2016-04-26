#!/bin/bash

nice -n 10 scrapy crawl -o tropes.json -s JOBDIR=crawls/tvtropes-4 tvtropes
