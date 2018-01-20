import scrapy

from tvtropes.items import TvtropesItem

class TvtropesSpider(scrapy.Spider):
    name = "tvtropes"
    allowed_domains = ["tvtropes.org"]
    start_urls = [
        "http://www.tvtropes.org/pmwiki/pmwiki.php/Main/Works"
    ]

    def parse(self, response):
        item = TvtropesItem()        
        
        #grab title - it's always in the same place
        title = response.xpath('//*[@id="body"]/div[9]/div[2]/div/div/div[2]/div/div/div[2]/div[1]/h1/text()').extract()
        title = [name.strip() for name in title]
        item['title'] = title

        #urls are better for naming but we grab the title to have something nice to display
        url_name = response.url.split("/")[-1]
        
        #namespace is the category tvtropes puts the page in; not used now, but could be useful
        namespace = response.url.split("/")[-2]

        #get all links in body - excludes index links at bottom, don't need them
        item['all_links'] = []
        content = response.xpath('//*[@id="body"]/div[9]/div[2]/div/div/div[2]/div/div/div[2]/div[3]')
        item['all_links'] = content.xpath('//a[contains(@class, "twikilink")]/@href').extract()
        
        #sets page type - if you can leave a review, it's a work; if there's 
        #"Creator" in the url, it's an actor/writer/etc.; otherwise it's a 
        #trope or an index; treating indexes like tropes because they're 
        #basically a trope bucket; if an index gets mentioned it could 
        #mean a group of tropes are more likely
        if len(response.css('.link-reviews').extract())>0:
            item['pageType'] = "Work"
            print "no reviews"
        elif len(response.css('.link-reviews.tuck-set').extract())>0:
            item['pageType'] = "Work"
            print "some reviews"
        elif "Creator" in response.url:
            item['pageType'] = "Creator"
        else:
            item['pageType'] = "Trope"

        #save item
        yield item

        #go follow all the links
        for link in item['all_links']:
            url = response.urljoin(link)
            yield scrapy.Request(url, self.parse)

