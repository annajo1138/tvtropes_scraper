#!/bin/bash

nice -n 10 scrapy crawl -o tropes_01-19-2018.json -s JOBDIR=crawls/tvtropes-1 tropes