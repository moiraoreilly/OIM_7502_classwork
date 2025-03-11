import scrapy
from stock_assignment.items import StockItem
# this isn't working, keep getting error "ImportError: cannot import name 'StockItem'
# from 'stock_assignment.items' (/Users/kevin/Desktop/Python/python_
# files/stock_assignment/stock_assignment/items.py)"

class SpnLoopSpider(scrapy.Spider):
    name = "spn_loop"
    allowed_domains = ["www.slickcharts.com"]
    start_urls = ["https://www.slickcharts.com/sp500/performance"]

    def parse(self, response):
        stock_assignment_item = StockItem()
        rows = response.xpath("//*[@class='table table-hover table-borderless table-sm']//tbody/tr")
        for row in rows:
            stock_assignment_item['number'] = row.xpath(".//td[1]/a/text()").get()
            stock_assignment_item['company'] = row.xpath(".//td[2]/a/text()").get()
            stock_assignment_item['symbol'] = row.xpath(".//td[3]/a/text()").get()
            stock_assignment_item['ytd_return'] = row.xpath(".//td[4]/text()").get()
            yield stock_assignment_item
