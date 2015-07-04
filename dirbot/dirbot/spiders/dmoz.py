# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from scrapy.selector import Selector
from dirbot.items import Website
import re
import json
import cPickle as pickle
from functools import partial


class DmozSpider(Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/",
    ]

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        sel = Selector(response)
        sites = sel.xpath('//ul[@class="directory-url"]/li')
        items = []
        # tmp = []

        for site in sites:
            item = Website()
            item['name'] = site.xpath('a/text()').extract()
            item['url'] = site.xpath('a/@href').extract()
            item['description'] = site.xpath('text()').re('-\s[^\n]*\\r')
            # tmp.append(dict(item))
            items.append(item)
        return items

        # print("=================================")
        # tmpStr = json.dumps(tmp)
        # print(tmpStr)
        # print("#################################")

        # start_url = response.url.rstrip('/').split('/')[-1];
        # regUrl = re.search(r'Books|Resources', start_url, re.IGNORECASE);
        #
        # if regUrl != None:
            # tmpFilename = regUrl.group(0);
            # filename = regUrl.group(0) + '.json';

            # tmpJsonItems = pickle.dumps(items)

            # with open(tmpFilename, 'w' ) as f:
            #     tmpJsonItems = pickle.dump(items, f)

            # with open(tmpFilename, 'r') as f:
            #     objItems = pickle.load(f)

            # print("=================================")
            # print(items)
            # # pp = partial(json.dumps, indent=1)
            # # pp(items)
            # print("#################################")
