import scrapy
import datetime

from tvtropes.items import TvtropesItem

class TropesSpider(scrapy.Spider):
    name = "tropes"
    allowed_domains = ["tvtropes.org"]
    start_urls = [
        "http://www.tvtropes.org/pmwiki/pmwiki.php/Main/Works"
    ]

    def parse(self, response):
        item = TvtropesItem()

        #name of the page, as per the url - this is the universal name
        item['url_name'] = response.url.split("/")[-1]

        #which subpart of TVTropes the page was from
        item['namespace'] = response.url.split("/")[-2]

        #get all links in body - excludes index links at bottom, don't need them
        item['all_links'] = []
        content = response.css('div.page-content')[0]

        # alleged new xpath, but let's try div.page-content first
        #'//*[@id="body"]/div[11]/div[2]/div/div/div[2]/div/div/div[2]/div[3]'

        # all internal tvtropes links
        item['all_links'] = content.css('a.twikilink::attr(href)').extract()

        # for kicks and giggles, see if being able to review actually does
        # correlate with page being for a work
        if len(response.css('.link-reviews').extract())>0:
            item['can_review'] = True
        elif len(response.css('.link-reviews.tuck-set').extract())>0:
            item['can_review'] = True
        else:
            item['can_review'] = False

        item['timestamp'] = datetime.datetime.now()

        #save item
        yield item

        #go follow all the links
        for link in item['all_links']:
            yield scrapy.Request(link, self.parse)
