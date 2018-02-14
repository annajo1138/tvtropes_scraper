#!/bin/bash

nice -n 10 scrapy crawl -o tropes_02-12-2018.json -s JOBDIR=crawls/tvtropes-3 tropes
