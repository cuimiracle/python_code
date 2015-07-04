# Scrapy settings for dirbot project

SPIDER_MODULES = ['dirbot.spiders']
NEWSPIDER_MODULE = 'dirbot.spiders'
DEFAULT_ITEM_CLASS = 'dirbot.items.Website'

ITEM_PIPELINES = {
    # 'dirbot.pipelines.FilterWordsPipeline': 1,
    'dirbot.pipelines.MySQLStorePipeline': 2,
}

MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'scrapydb'
MYSQL_USER = 'root'
MYSQL_PASSWD = ''